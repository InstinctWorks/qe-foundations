# Retrospective -- Thursday pair exercise (SQL validation)

<!--
HOW TO USE: copy this file to  qe_foundations/docs/retrospective.md  and answer every
"##" section below (keep the headings). Write TOGETHER in the last 15 minutes; both
partners must agree with what is written. Aim for 2-4 specific sentences per section
(about 250-400 words in total). "It went well" is not an answer: name a rule, a
moment, a query, a commit.
Delete nothing except these comments.
-->

## Pair and branch

<!-- Names of both partners, the repo + branch you worked on, the final commit hash. -->
Antoine Tran
George George

Repo: qe-foundations (Owner: Antoine)
Branch: feature/sql-validation-antoine-george

Final Commit Hash: deaa72e55ff4a1f7d9eab7ce90c5608be1303402

## What we built

<!-- In your own words: what is in the repo now (queries, runner, tests, docs)? How many rules did your suite end with, and what does one `python -m qe_foundations.validation` run print? -->

We implemented 12 SQL validation rules (R-01 through R-12) and two expectation rules (E-01 through E-02) to identify data-quality issues in test runs. We also worked on the Python validation runner, including custom expectations, logging and execution of SQL rules. 

Running python -m qe_foundations.validation displays each rule's PASS, FAIL, or INFO status, evidence for failed rules, and a final summary. We also worked on unit tests and documentation to record our findings.

## How the pairing worked

<!-- Did the driver/navigator split and the 30-minute swaps work? Give one concrete moment where the navigator caught something the driver would have missed, and one moment the pairing felt awkward or slow. What did you change as a result? -->

The driver/navigator split worked smoothly. A moment where the navigator helped catch mistakes while writing SQL violation queries, particularly when checking conditions and expected results. Pairing felt slower during the Python runner because debugging required more careful attention. We addressed this by reviewing the check_exercise.py results and Python tracebacks together to identify and resolve errors.

## The hardest rule

<!-- Which rule (R-xx) took longest, and why? Quote the first wrong version of the query and what it returned (too many rows? none? an error?), then what fixed it. -->
R-09 took the longest because had issues figuring out the pattern to check the vailidity of the timestamp.

First Version: "YYYY-MM-DD HH-MM-SS"
Returned: None

Fixed Version: "%____-__-__ __-__-__%"

## A surprise in the data

<!-- Which defect did you NOT expect, or which "defect" turned out to be a legitimate row (a false alarm you avoided or briefly fell for)? What would you ask the product owner about it? -->
We were surprised that run 5012 was marked PASSED but had a slow-response warning in `failure_message`; we would ask the product owner whether warnings belong in that field or should be stored separately.

## SQLite and SQL pitfalls we hit

<!-- NULL behaviour, case sensitivity of = / IN versus LIKE, trailing spaces, inclusive BETWEEN, AND/OR precedence... Which of these bit you, and how will you spot it next time? -->

AND/OR precedence and NULL behavior caused confusion when constructing validation conditions. We learned that to distinguish between violation queries, which search for invalid records, and expectation queries, which verify required records exist. Next time, we would break complicated conditions into smaller parts and compare the returned rows against expected results.

## Skills we connected from this week

<!-- Name one thing each from Monday (modules/venv/Git), Tuesday (exceptions/files), Wednesday (logging/unittest/merge conflicts) that you actually used today, and how. -->

From Monday, we used Git branches, commits, and the Python virtual environment to manage our shared project. From Tuesday, we applied custom exception handling through ValidationFailedError and worked with SQL and Python files. From Wednesday, we used Python logging and unit testing concepts to build and verify the validation runner. These concepts came together into a single workflow for detecting and reporting data-quality problems.

## What we would do differently

<!-- One process improvement for the next pair session, and one thing you need from Friday (joins, GROUP BY, constraints) to make this validation suite better. -->

For our next pairing session, we would allocate more time for testing, logging and documentation instead of leaving them until the end.For Friday, we want to improve the validation suite using SQL JOINs and GROUP BY to identify inconsistencies across related tables, as well as constraints to prevent invalid data from being inserted.
