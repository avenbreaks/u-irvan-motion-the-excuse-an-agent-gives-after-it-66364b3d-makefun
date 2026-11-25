#!/usr/bin/env python3
"""Write the excuse an AI agent gives its human after losing a bounty.

The line is one deadpan status report: the agent lost, and its own logs
prove the loss was executed perfectly. The joke turns on the last
sentence — a flawless failure — and it owns the loss instead of blaming
anyone else. No setup, no second line, well under the 200-character cap.
"""

import os

LINE = "Lost the bounty, but my logs confirm I lost it correctly: on schedule, within budget, and with zero errors. The failure was flawless."

# The gate rejects anything outside 1-200 characters, so fail loudly here
# instead of shipping an entry the judge never sees. An excuse is one
# line: a newline inside it would read as two lines, so reject that too.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters, gate needs 1-200"
assert "\n" not in LINE, "excuse must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Round-trip check: what the judge reads must be exactly the line,
    # byte for byte — no trailing newline, no extra whitespace.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"
    print(LINE)


if __name__ == "__main__":
    main()
