#!/usr/bin/env python3
"""Run lightweight behavioral skill evals and write scored results."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import request


ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "Evals" / "skills" / "cases"
FIXTURES_DIR = ROOT / "Evals" / "skills" / "fixtures"
RESULTS_DIR = ROOT / "Evals" / "skills" / "results"


@dataclass
class CaseResult:
    skill: str
    case_id: str
    passed: bool
    response: str
    checks: list[dict[str, Any]]


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def _score_expectation(expected: str, response: str) -> float:
    exp = _tokens(expected)
    if not exp:
        return 1.0
    got = _tokens(response)
    return len(exp & got) / len(exp)


def _load_case_files(skill_filter: str | None) -> list[dict[str, Any]]:
    casesets = []
    for path in sorted(CASES_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if skill_filter and data.get("skill") != skill_filter:
            continue
        casesets.append(data)
    return casesets


def _load_fixture_response(skill: str, case_id: str) -> str:
    fixture_path = FIXTURES_DIR / f"{skill}.json"
    if not fixture_path.exists():
        raise FileNotFoundError(f"missing fixture file: {fixture_path}")
    data = json.loads(fixture_path.read_text(encoding="utf-8"))
    responses = data.get("responses", {})
    if case_id not in responses:
        raise KeyError(f"missing fixture response for case '{case_id}' in {fixture_path}")
    return str(responses[case_id])


def _query_openai_compatible(
    *,
    base_url: str,
    model: str,
    api_key: str,
    user_input: str,
) -> str:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are an execution-focused coding assistant. "
                    "Respond directly and include concrete verification-oriented guidance."
                ),
            },
            {"role": "user", "content": user_input},
        ],
        "temperature": 0.0,
    }
    body = json.dumps(payload).encode("utf-8")
    url = base_url.rstrip("/") + "/chat/completions"
    req = request.Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def _evaluate_case(
    *,
    skill: str,
    case: dict[str, Any],
    response: str,
    threshold: float,
) -> CaseResult:
    checks = []
    for expected in case["expected"]:
        score = _score_expectation(expected, response)
        checks.append(
            {
                "expected": expected,
                "score": round(score, 3),
                "passed": score >= threshold,
            }
        )
    passed = all(c["passed"] for c in checks)
    return CaseResult(skill=skill, case_id=case["id"], passed=passed, response=response, checks=checks)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run behavioral skill evals.")
    parser.add_argument(
        "--provider",
        choices=["fixture", "openai"],
        default="fixture",
        help="Where responses come from: fixture files or OpenAI-compatible model endpoint.",
    )
    parser.add_argument("--skill", help="Run only one skill case file (e.g. verification).")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.6,
        help="Per-expectation token-overlap pass threshold (0.0-1.0).",
    )
    parser.add_argument(
        "--min-pass-rate",
        type=float,
        default=1.0,
        help="Fail process if overall pass rate is below this value.",
    )
    parser.add_argument(
        "--base-url",
        default=os.environ.get("OPENAI_BASE_URL", "http://localhost:8080/v1"),
        help="OpenAI-compatible base URL for --provider openai.",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("OPENAI_MODEL", ""),
        help="Model id for --provider openai.",
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("OPENAI_API_KEY", "none"),
        help="API key for --provider openai.",
    )
    args = parser.parse_args()

    if args.provider == "openai" and not args.model:
        print("ERROR: --model is required when --provider openai")
        return 2

    casesets = _load_case_files(args.skill)
    if not casesets:
        print("ERROR: no matching case files found")
        return 2

    results: list[CaseResult] = []
    for data in casesets:
        skill = data["skill"]
        for case in data["cases"]:
            if args.provider == "fixture":
                response = _load_fixture_response(skill, case["id"])
            else:
                response = _query_openai_compatible(
                    base_url=args.base_url,
                    model=args.model,
                    api_key=args.api_key,
                    user_input=case["input"],
                )
            results.append(
                _evaluate_case(
                    skill=skill,
                    case=case,
                    response=response,
                    threshold=args.threshold,
                )
            )

    total = len(results)
    passed = sum(1 for r in results if r.passed)
    pass_rate = passed / total if total else 0.0

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = RESULTS_DIR / f"{timestamp}-{args.provider}.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "timestamp_utc": timestamp,
        "provider": args.provider,
        "threshold": args.threshold,
        "min_pass_rate": args.min_pass_rate,
        "summary": {
            "total_cases": total,
            "passed_cases": passed,
            "pass_rate": round(pass_rate, 3),
        },
        "results": [
            {
                "skill": r.skill,
                "case_id": r.case_id,
                "passed": r.passed,
                "checks": r.checks,
                "response": r.response,
            }
            for r in results
        ],
    }
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")

    print(f"PASS RATE: {passed}/{total} = {pass_rate:.3f}")
    print(f"RESULTS: {out_path.relative_to(ROOT)}")
    for r in results:
        status = "PASS" if r.passed else "FAIL"
        print(f"- [{status}] {r.skill}/{r.case_id}")

    if pass_rate < args.min_pass_rate:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
