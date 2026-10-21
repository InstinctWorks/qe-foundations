"""qe_foundations/ingestion/readers.py  -  TASK 4 (about 35 min)

One reader per format. Each returns a LIST OF RAW RECORDS and only deals with
FORMAT problems (is this valid CSV / JSON / XML? are the columns there?).
Business rules (is the status allowed? is the duration negative?) belong to
validation.py, NOT here.

Always open files through open_source() from contexts.py.
See README Task 4 for the exact contract of each reader.
"""

import csv
import json
import xml.etree.ElementTree as ET

from .contexts import open_source
from .exceptions import MalformedSourceError, MissingColumnsError
from .validation import REQUIRED_FIELDS


def read_csv_records(path):
    """CSV -> list of raw dicts, one per data row (use csv.DictReader)."""

    with open_source(path) as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise MissingColumnsError(path, REQUIRED_FIELDS)

        missing = [
            field for field in REQUIRED_FIELDS
            if field not in reader.fieldnames
        ]

        if missing:
            raise MissingColumnsError(path, missing)

        return list(reader)


def read_json_records(path):
    """JSON -> list of raw records. Expected shape: {"suite": ..., "tests": [...]}."""
    
    try:
        with open_source(path) as file:
            data = json.load(file)

    except json.JSONDecodeError as e:
        raise MalformedSourceError(
            path, f"Invalid JSON at line {e.lineno}: {e.msg}"
        ) from e

    if not isinstance(data, dict):
        raise MalformedSourceError(path, "JSON root must be an object")

    if "tests" not in data or not isinstance(data["tests"], list):
        raise MalformedSourceError(path, "JSON must contain a 'tests' list")

    return data["tests"]


def read_xml_records(path):
    """XML -> list of raw dicts, one per <testcase> element at ANY depth."""

    try:
        with open_source(path) as file:
            tree = ET.parse(file)
            root = tree.getroot()

    except ET.ParseError as e:
        raise MalformedSourceError(path, f"Invalid XML: {e}") from e

    records = []

    for testcase in root.iter("testcase"):
        record = {
            "id": testcase.get("id"),
            "title": testcase.findtext("title"),
            "status": testcase.get("status"),
            "duration": testcase.findtext("duration"),
        }
        records.append(record)

    return records
