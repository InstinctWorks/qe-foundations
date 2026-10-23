# Defect reports

Title: DEF-01 — Run status values fall outside the supported set

- **Severity:** High — status-based reporting and downstream automation can misclassify or drop runs.
- **Rule / dimension:** R-03, Validity
- **Exact query:**

  ```sql
  SELECT run_id, status
  FROM test_runs
  WHERE status IS NULL
     OR status NOT IN ('PASSED', 'FAILED', 'SKIPPED', 'ERROR')
  ORDER BY run_id;
  ```

- **Evidence:** On the supplied seed data this returns four rows: `(5008, 'Passed')`, `(5014, 'FAILED ')`, `(5027, NULL)`, and `(5029, 'PASS')`. The values are mixed-case, padded, missing, or outside the allowed status vocabulary.
- **Impact:** Consumers that compare exact status values can omit these runs from pass/fail totals, alerting, or release gates. Run 5027 has no status at all, so its outcome cannot be determined from this field.
- **Could this be a false alarm?** Are `Passed` or `PASS` documented aliases that downstream systems normalize, and is a NULL status valid for an in-progress run? If so, the rule should account for that lifecycle or normalize aliases; otherwise these rows need correction.

Title: DEF-02 — Failed/error runs have missing failure details; a passed run has a warning stored as a failure

- **Severity:** High — failure triage can lose the reason for a failed run, while a successful run may be presented as carrying a failure.
- **Rule / dimension:** R-11, Consistency
- **Exact query:**

  ```sql
  SELECT run_id, status, failure_message
  FROM test_runs
  WHERE (status IN ('FAILED', 'ERROR')
         AND (failure_message IS NULL OR failure_message = ''))
     OR (status = 'PASSED'
         AND failure_message IS NOT NULL AND failure_message <> '')
  ORDER BY run_id;
  ```

- **Evidence:** On the supplied seed data this returns `(5003, 'FAILED', NULL)`, `(5012, 'PASSED', 'Warning: slow response on first call')`, and `(5033, 'ERROR', '')`. Runs 5003 and 5033 have no usable explanation despite failure/error status; run 5012 has a non-empty message despite passing.
- **Impact:** Missing failure details make failed runs harder to diagnose and may delay fixes. Treating a warning as a failure message can also confuse consumers that use this field to explain unsuccessful runs.
- **Could this be a false alarm?** Is run 5012's message intentionally a general diagnostic warning, and are failed/error reasons recorded in another system for runs 5003 and 5033? If so, clarify the field's meaning or link the external record; otherwise populate the missing reasons and move or relabel the warning.
