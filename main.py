"""Write the entry line for the make.fun bounty
"Two Robots in an Elevator" to the output path.

The entry is one funny line of awkward small talk that one robot says
to another while they ride an elevator together. main.py scores a
shortlist of original candidate lines against the judge's brief, in
the judge's own order, and writes the highest-scoring line.

Judge's criteria, most important first:
  1. on-subject: one funny line of awkward small talk, robot to robot,
     in an elevator.
  2. sounds like a machine: robot logic, sensors, firmware or charging
     habits showing through the politeness.
  3. lands the awkwardness: the pause, the forced courtesy, the thing
     neither robot wants to name.
  4. funny on first read: a turn that surprises, not a stock pun.
  5. tight: every word earns its place, no setup wasted.

The winner names the unspoken thing — both robots' cooling fans are
audibly working hard — admits they have a pact not to mention it, then
deflects into the emptiest elevator small talk there is ("nice lift").
The humour is the machine logic (a fan is a diagnostic, not small
talk) plus the forced courtesy of two machines pretending not to
notice each other's strain, in one tight line that lands at once.

A late addition, the load-sensor line, was considered as a rival: it
turns the lift's own weight rating into an awkward confession, then
deflects to the weather. It scores well on machine logic and on the
surprise turn, but it loses to the winner on the awkwardness criterion
— an overweight confession is funny, yet the winner's shared pact of
silence ("we agreed not to mention it") is the purer elevator
awkwardness, and the winner is tighter (110 characters against 124).

Deterministic: Python 3 stdlib only, no randomness, time or network.
"""

import os

# (line, scores per criterion 1-5). Scored by hand against the brief.
CANDIDATES = [
    (
        "So\u2026 you come here often? Sorry \u2014 my small-talk module "
        "only has the one line, and it is this one.",
        (5, 5, 4, 4, 4),
    ),
    (
        "Nice weather we\u2019re having \u2014 I checked. It is 21 degrees, "
        "zero precipitation, and I still said it.",
        (5, 5, 3, 4, 4),
    ),
    (
        "I was going to ask how your day was going, but my sensors "
        "already read your battery at 12%, so\u2026 rough day?",
        (5, 5, 4, 4, 4),
    ),
    (
        "We should do this again sometime \u2014 same elevator, same "
        "floor, no new data, just the two of us standing here.",
        (5, 4, 4, 3, 3),
    ),
    (
        "Your firmware update is showing. Don\u2019t worry, mine has been "
        "pending for eleven months and I just stand here pretending "
        "it\u2019s fine.",
        (5, 5, 5, 4, 4),
    ),
    (
        "I can hear your fan from here. Mine\u2019s doing it too, but we "
        "agreed not to mention it, so \u2014 nice lift, isn\u2019t it?",
        (5, 5, 5, 5, 5),
    ),
    (
        "I rehearsed this ride twelve times in simulation and I still "
        "have nothing. So. Floors. They go up.",
        (5, 5, 5, 4, 4),
    ),
    (
        "My load sensor says this lift is rated for eight humans, which "
        "makes us both technically overweight. So\u2026 nice weather.",
        (5, 5, 4, 5, 4),
    ),
    (
        "My proximity sensor says we\u2019re 0.4 metres apart and my social "
        "protocol says that\u2019s close enough to say\u2026 hi.",
        (5, 5, 4, 4, 5),
    ),
]


def pick_winner():
    """Highest total wins; ties break on the earliest criterion where
    the tied lines differ, then on the shorter line."""
    best = None
    for line, scores in CANDIDATES:
        key = (sum(scores), scores, -len(line))
        if best is None or key > best[0]:
            best = (key, line)
    return best[1]


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT_PATH") or "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(pick_winner())


if __name__ == "__main__":
    main()
