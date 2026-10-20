# QE Foundations

A Python utility library for generating and validating QA test data, serving as the foundation for Revature Project 1.

## Project 1 milestone - Week 2, Monday

The Monday milestone establishes the repository, reusable Python utility package, virtual environment, and dependency management.

**Completed Monday:**
- Created the `qe_foundations` Python package and `utils` sub-package.
- Organized string, number, date, and test-data generation utilities into separate modules.
- Implemented `mask_email()` and `days_between()`.
- Configured `requirements.txt` and `requirements-dev.txt`.
- Added a smoke test and project documentation.

**Upcoming work:**
- **Tuesday:** Add data ingestion and validation in `qe_foundations/ingestion/`.
- **Wednesday:** Add logging and automated unit tests using PyTest.
- **Thursday:** Add SQL data-validation queries in `sql/`.
- **Friday:** Add joins validation and integration testing.

## Setup

Follow these steps from the project root after cloning the repository.

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Bash (Linux/macOS):**

```bash
source .venv/bin/activate
```

**Git Bash on Windows:**

```bash
source .venv/Scripts/activate
```

### 3. Install dependencies

For runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

For development dependencies, including PyTest:

```bash
python -m pip install -r requirements-dev.txt
```

### 4. Verify the installation

Run the provided smoke test:

```bash
python smoke_utils.py
```

Expected result: `7/7 checks passed`.

## Usage

Import the reusable utility functions from `qe_foundations.utils`:

```python
from datetime import date
from qe_foundations.utils import slugify, mask_email, days_between, make_users

print(slugify("  Login Page: Happy Path "))
# login-page-happy-path

print(mask_email("tester@example.com"))
# t***@example.com

print(days_between(date(2025, 1, 1), date(2025, 1, 31)))
# 30

print(make_users(2, seed=1))
# Generate two reproducible sample users
```

## Repository Structure

- `qe_foundations/` — Main Python package.
- `qe_foundations/utils/` — Reusable utility modules.
- `tests/` — Automated tests (starting Wednesday).
- `data/` — CSV/JSON test data (starting Tuesday).
- `docs/` — Project documentation.

See `docs/structure.md` for more information.

## Project Status

Week 2 Monday: utility package implemented and smoke tests passing locally. Remote repository publishing and fresh-clone verification are part of the remaining kickoff work.