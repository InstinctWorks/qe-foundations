"""qe_foundations/ingestion/validation.py  -  TASK 5 (about 25 min)

validate_record() decides whether ONE raw record is acceptable.

IMPORTANT: this is VALIDATION OF EXTERNAL DATA. Raise exceptions here.
Do NOT use `assert` in this file (assertions can be switched off with `python -O`).
See README Task 5 for the exact rules.
"""

import math  # Step 4 Added this

from .exceptions import InvalidValueError, MissingFieldError

REQUIRED_FIELDS = ("id", "title", "status", "duration")
VALID_STATUSES = ("pass", "fail", "blocked")


def validate_record(row, raw):
    """Turn one raw record into a clean dict, or raise a RecordValidationError.

    row : 1-based record number in the file (used in error messages)
    raw : whatever the reader produced for that record (usually a dict)

    Returns {"id": str, "title": str, "status": str, "duration": float}.
    """

    if not isinstance(raw, dict):
        raise InvalidValueError(
            row, "record", raw, "a dictionary"
        )

    for field in REQUIRED_FIELDS:
        value = raw.get(field)

        if value is None or (isinstance(value, str) and not value.strip()):
            raise MissingFieldError(row, field)

    for field in ("title", "status"):
        if not isinstance(raw[field], str):
            raise InvalidValueError(row, field, raw[field], "a string")

    test_id = str(raw["id"]).strip()
    title = raw["title"].strip()
    status = raw["status"].strip().lower()

    if status not in VALID_STATUSES:
        raise InvalidValueError(
            row, "status", raw["status"], f"one of {VALID_STATUSES}"
        )

    duration_value = raw["duration"]

    if isinstance(duration_value, bool):
        raise InvalidValueError(row, "duration", duration_value, "a non-negative finite number")

    try:
        duration = float(duration_value)
    except (TypeError, ValueError) as e:
        raise InvalidValueError(
            row, "duration", duration_value, "a non-negative finite number"
        ) from e

    if not math.isfinite(duration) or duration < 0:
        raise InvalidValueError(row, "duration", duration_value, "a non-negative finite number")

    return {"id": test_id, "title": title, "status": status, "duration": duration}