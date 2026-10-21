# Ingestion module - design notes (Week 2, Day 2)

Answer in your own words, 2-4 sentences each. Replace every line that starts with

## 1. Exceptions or assertions?
In `validate_record` I raise exceptions for a negative duration, but in `IngestionReport.check_invariants` I use `assert`. Why is each the right tool there?

Exceptions are used in `validate_record` because invalid data can come from external files, and the program needs to handle it properly. Assertions are used in `check_invariants` to catch mistakes in the program's internal bookkeeping. Assertions can also be disabled, so they should not be used for validating input data.

## 2. Stop or collect?
Why is a malformed JSON file a `SourceError` that stops loading, while a record with a bad status is a `RecordValidationError` that is collected? Who benefits from this split?

A malformed JSON file cannot be parsed properly, so the entire file needs to stop loading. A record with an invalid status only affects that individual record, allowing the remaining records to continue processing. This helps users identify bad records without losing valid data from the same file.

## 3. What did the context managers buy you?
Name two things that `open_source` / `LoadSession` do for the caller that you would otherwise have to remember to do at every call site.

`open_source` automatically closes files and converts file-related errors into our custom exceptions. `LoadSession` tracks how long an operation takes and whether it completed successfully or failed. This avoids having to repeat those steps every time a file is loaded.

## 4. Your hardest bad-input case
Which sample file or record took you longest to handle, and what was the cause?

The messy test-case data was the most challenging because it contained different types of invalid records, including missing fields, invalid values, and duplicate IDs. I had to make sure each invalid record was rejected correctly while allowing valid records to continue processing.