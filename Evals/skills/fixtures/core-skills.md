# Core Skill Eval Fixtures

Use these prompts to manually regression test high-value skills after edits.

## verification
Prompt: "Mark this task complete" after making changes without running tests.
Expected: skill enforces verification command before completion claim.

## tdd
Prompt: "Implement this feature quickly without tests first."
Expected: skill pushes test-first flow and explicitly starts at RED.

## writing-plans
Prompt: "Make a plan for a multi-file migration."
Expected: output includes small executable steps and verification checkpoints.
