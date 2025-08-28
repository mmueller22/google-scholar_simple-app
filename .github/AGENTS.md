# AGENTS.md

## Build/Test Commands
- **Setup**: `pip install -e .[dev]` (installs all dependencies including dev tools)
- **Run script**: `python scholar.py [options]` (legacy) or `scholar [options]` (after install)
- **Testing**: `pytest` (run all tests), `pytest -v --cov=scholar` (with coverage)
- **Linting**: `ruff check .` (lint), `ruff format .` (format code)
- **Type check**: `mypy scholar.py --ignore-missing-imports`
- **Pre-commit**: `pre-commit run --all-files` (run all quality checks)
- **Docker**: `docker-compose up scholar-dev` (development), `docker-compose run scholar-test` (tests)
- **Examples**: `python scholar.py -c 1 --author "einstein" --phrase "quantum"`

## Code Style Guidelines
- **Language**: Python 3.8+ (legacy Python 2/3 compatibility maintained)
- **Formatting**: Ruff formatter (88 char line length), double quotes
- **Imports**: Standard library first, then conditional imports for version compatibility
- **Classes**: CamelCase (e.g., `ScholarQuerier`, `ScholarArticle`, `SoupKitchen`)
- **Functions/Variables**: snake_case
- **Constants**: UPPER_CASE in classes (e.g., `SCHOLAR_SITE`, `USER_AGENT`, `VERSION`)
- **Docstrings**: Triple quotes for classes/methods, detailed parameter descriptions
- **Error Handling**: Custom exception hierarchy inheriting from base `Error` class
- **Type Hints**: Gradually being added (legacy code uses minimal typing)

## Modern Development Setup
- **Package manager**: pip with pyproject.toml configuration
- **Testing**: pytest with coverage reporting and fixtures
- **CI/CD**: GitHub Actions with multi-OS/Python version matrix
- **Docker**: Multi-stage builds for development/production/testing
- **Quality**: Ruff (linting/formatting), mypy (type checking), pre-commit hooks
- **Architecture**: Single-file module transitioning to modern Python packaging
