# Python Template

Simple Python template with pytest, black, and flake8

This is a super simple template for python3.11.
It includes configs for VSCode (test runner config and project config)

## Getting Started

- Install poetry first
- `python3.11 -m venv venv` (to create virtualenv)
- Install `poetry` if needed
- Development: poetry install --with jupyter
  - `with --jupyter` only if you need notebooks
- Production: poetry install --only main

## Includes

- Uses `poetry` as package manager
- Tests integrated in VSCode (tests panel)
- Sorts out PYTHONPATHs
  - tests
  - notebooks
  - vscode debugger
- Notebook imports from venv working
- `black` for formatting
- `flake8` for linting

## `requirements.txt` generation

```bash
poetry export --without-hashes --with dev --format=requirements.txt > requirements.txt
```
