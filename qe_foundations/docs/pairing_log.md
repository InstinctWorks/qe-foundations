# Pairing log -- roles and swap schedule

<!--
HOW TO USE: copy this file to  qe_foundations/docs/pairing_log.md.
Fill ONE row at the END of every 30-minute block (it takes one minute). The check
script counts the rows that are filled in; a 3-hour session has 5 driving blocks.
-->

## Roles card (keep it visible)

| | DRIVER | NAVIGATOR |
|---|---|---|
| Hands | the ONLY one on the keyboard | off the keyboard |
| Job | turn the navigator's direction into code; think aloud while typing | read the rule, decide the next step, predict the result, spot typos and edge cases |
| Says things like | "I'm writing the WHERE clause now..." | "Predict first: which run_ids do we expect?" |
| Never | silently type something nobody asked for | grab the mouse or dictate character by character |

**Swap** every 30 minutes, even in the middle of a rule. The outgoing driver commits and pushes
(your own Git name), the new driver runs `git pull`, then types.

## Pair

| | Name | Git user.name (as shown by `git log`) | Machine / repo owner |
|---|---|---|---|
| Partner A | Antoine Tran| instinctworks | Repo owner |
| Partner B | George George| georggeo | Machine |

Branch: `feature/sql-validation-...`        Remote: ...

## Swap log (one row per block)

| Block | Clock time | Driver | Navigator | Goal of the block | Result (rules done, commit hash) | Predictions: right / wrong |
|---|---|---|---|---|---|---|
| 1 | 00:00 - 30:00 | George | Antoine | Correctness of the queries | R01-R04, 5e6cc4f5b116c443bc39a9706c11bb53ccd1e054| wrong |
| 2 | 30:00 - 60:00| Antoine | George | Accuracy of the queries | R05-R08, 776fcfcda1d92cc9eb26a6f6bc4e9ef26037d988 | right|
| 3 | 60:00 - 90:00| George | Antoine | Consistency checck of the queries | R09-R012 E01-E02, bb5365331505c8ffcb8c3d17cd1df3ee52306d11 |right |
| 4 | 90:00 - 120:00| Antoine | George | Logging | Python runner, e5630975b5f3822c30c432ed2fee8c9aede0cf9f | right|
| 5 | 120:00 - 150:00| George | Antoine | | Tests, checklists, reports | wrong|

## Disagreements and how we settled them

<!-- At least one honest example: what did you disagree about (query style, a rule's meaning, ...), and how did you decide? --> 
There were disagreements over the basic python syntax when fixing the queries on the rules. It was either an oversimplification or complexity.

## Hints we used

<!-- Which hint levels, for which rules? (Using hints is fine -- hiding it is not.) -->
Most of the hints we used where a mixture of the written notes in the github, some research for the clauses and ultimately when we were stuck we used ai.

