# Expected-defect checklist (fill in as you go)

<!--
PURPOSE: this is your "answer sheet" for the data. Writing the PREDICTION before you run a
query is the single best habit for catching false passes.
HOW: for each rule, (1) write what you EXPECT in the "Predicted" column BEFORE running the
query, (2) run it, (3) write the run_ids it actually returned in "Defects found (run_ids)"
(comma-separated, 4-digit ids), (4) note anything surprising. Do not delete rows.
check_exercise.py compares this table with what your queries return.
-->

| Rule | Defects found (run_ids) | Predicted (before running) | Notes / surprises |
|---|---|---|---|
| R-01 | 5006, 5019, 5025 | 3 rows | NULL, empty, and whitespace-only executor values are all missing. |
| R-02 | 5011, 5022 | 2 rows | One address has no @; `tom@qa` has no dot after @. |
| R-03 | 5008, 5014, 5027, 5029 | 4 rows | Mixed case, trailing space, NULL, and unsupported `PASS`. |
| R-04 | 5009, 5016 | 2 rows | Negative duration and NULL duration. Zero remains legal. |
| R-05 | 5030, 5023 | 2 rows | Both exceed 600000 ms; ordered largest first. |
| R-06 | 5013, 5020 | 2 rows | Retry count is -1 and 7, respectively. |
| R-07 | 5017, 5024, 5026 | 3 rows | Unsupported PROD, lower-case qa, and NULL environment. |
| R-08 | 5014, 5018, 5028 | 3 rows | Stray spaces in status, test_name, and suite. |
| R-09 | 5010, 5015, 5035 | 3 rows | Malformed start time, malformed finish time, and missing finish time. |
| R-10 | 5005, 5032 | 2 rows | Run 5005 finishes before it starts; run 5032 is future-dated. |
| R-11 | 5003, 5012, 5033 | 3 rows | Missing failure details on FAILED/ERROR, plus a message on PASSED. |
| R-12 | 5031, 5034, 5036, 5037 | 4 rows | Invalid width, lower-case prefix, NULL, and missing dash. |

## Decoys: rows that look odd but are LEGAL (we must not flag them)

* Run 5004: `SKIPPED` with 0 ms is valid; skipped tests can take no time.
* Run 5041: exactly 600000 ms is not an R-05 outlier because the rule flags values above, not equal to, ten minutes.


## Rows reported by more than one rule

* Run 5014 appears in R-03 (unsupported status `FAILED `) and R-08 (trailing space). This overlap is expected: each rule checks a separate data-quality property.


## Open questions for the product owner

* R-05's 10-minute outlier threshold is a review threshold; confirm whether it should vary by test or suite.
* R-11 treats every non-empty message on a PASSED run as inconsistent. Confirm whether informational warnings, such as run 5012's slow-response note, belong in a separate field.

