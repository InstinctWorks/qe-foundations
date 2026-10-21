"""qe_foundations/ingestion/exceptions.py  -  TASK 2 (about 25 min)

The exception hierarchy for the data-ingestion module. Target tree:

    IngestionError
    +-- SourceError                 the FILE is unusable      -> stop loading that file
    |   +-- SourceNotFoundError
    |   +-- SourceUnreadableError
    |   +-- UnsupportedFormatError
    |   +-- MalformedSourceError
    |   +-- MissingColumnsError
    +-- RecordValidationError       ONE RECORD is bad         -> reject it, keep going
        +-- MissingFieldError
        +-- InvalidValueError
        +-- DuplicateIdError

Already done for you: IngestionError, SourceError, SourceNotFoundError and
RecordValidationError. They show the pattern (store useful attributes, build a
readable message, call super().__init__).

YOUR JOB: replace every `pass  # TODO` below with a real class body.
See README Task 2 for the exact attributes and message rules.
"""

from pathlib import Path


class IngestionError(Exception):
    """Base class: `except IngestionError` catches everything this module raises."""


# ---- The whole source (file) is unusable ----------------------------------
class SourceError(IngestionError):
    """A file as a whole cannot be used. Carries the path and a detail text."""

    def __init__(self, path, detail):
        self.path = str(path)
        self.detail = detail
        super().__init__(f"{Path(path).name}: {detail}")


class SourceNotFoundError(SourceError):
    """EXAMPLE (done for you): the file does not exist."""

    def __init__(self, path):
        super().__init__(path, "file not found")


class SourceUnreadableError(SourceError):
    
    def __init__(self, path, os_error):
        detail = f"cannot be read ({type(os_error).__name__})"
        super().__init__(path, detail)


class UnsupportedFormatError(SourceError):
    
    def __init__(self, path, suffix):  # must store `self.suffix`.
        self.suffix = suffix
        super().__init__(path, f"unsupported file format: {suffix}")


class MalformedSourceError(SourceError):

    def __init__(self, path, detail):
        super().__init__(path, detail)


class MissingColumnsError(SourceError):
    # a CSV file lacks required columns.

    def __init__(self, path, missing):  # must store `self.missing` as a list.
        self.missing = list(missing)
        super().__init__(path, f"Missing columns: {', '.join(self.missing)}")

    pass  # TODO


# ---- One record is invalid -------------------------------------------------
class RecordValidationError(IngestionError):
    """One record is invalid. `row` is the 1-based record number in the file."""

    def __init__(self, row, field_name, message):
        self.row = row
        self.field = field_name
        super().__init__(f"Row {row}: {message}")


class MissingFieldError(RecordValidationError):
    # a required field is absent, None, or blank.

    def __init__(self, row, field_name):
        super().__init__(row, field_name, f"Missing required field: {field_name}")


class InvalidValueError(RecordValidationError):
    # a field is present but its value is not acceptable.

    def __init__(self, row, field_name, value, expected):  # store `self.value` and `self.expected`.
        self.value = value
        self.expected = expected
        super().__init__(row, field_name, f"{value} is not acceptable. Expected: {expected}")


class DuplicateIdError(RecordValidationError):
    # the same test id appeared earlier in the file.

    def __init__(self, row, test_id):  # store `self.test_id`; the field is "id".
        self.test_id = test_id
        super().__init__(row, "id", f"{test_id} appeared earlier in the file")
