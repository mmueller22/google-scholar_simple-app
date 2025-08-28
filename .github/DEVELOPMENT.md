# Development Setup Guide

## Quick Start

### Using Python Virtual Environment

```bash
# Clone the repository
git clone https://github.com/mmueller22/google-scholar_simple-app.git
cd google-scholar_simple-app

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e '.[dev]'

# Set up pre-commit hooks
pre-commit install

# Run tests to verify setup
pytest

# Run the tool
python scholar.py --help
```

### Using Docker

```bash
# Development environment with hot reloading
docker-compose up scholar-dev

# Run tests in Docker
docker-compose run scholar-test

# Production build
docker-compose up scholar-prod

# Interactive Jupyter notebook (optional)
docker-compose up scholar-notebook
# Access at http://localhost:8888
```

## Development Commands

### Testing
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=scholar --cov-report=html

# Run specific test file
pytest tests/test_scholar_basic.py

# Run tests in Docker
docker-compose run scholar-test
```

### Code Quality
```bash
# Lint code
ruff check .

# Format code
ruff format .

# Type checking
mypy scholar.py --ignore-missing-imports

# Run all pre-commit hooks
pre-commit run --all-files
```

### Docker Commands
```bash
# Build all images
docker-compose build

# Run development container
docker-compose run --rm scholar-dev bash

# View logs
docker-compose logs scholar-dev

# Clean up
docker-compose down
docker system prune
```

## Project Structure

```
scholar.py/
├── scholar.py              # Main module
├── pyproject.toml          # Project configuration
├── Dockerfile              # Multi-stage Docker build
├── docker-compose.yml      # Development services
├── .pre-commit-config.yaml # Git hooks configuration
├── tests/                  # Test suite
│   ├── conftest.py         # Test fixtures
│   ├── test_scholar_basic.py
│   └── fixtures/
│       └── sample_data.py  # Mock data
├── .github/
│   ├── workflows/ci.yml    # CI/CD pipeline
│   └── AGENTS.md          # Agent guidelines
└── README.md              # Documentation
```

## Environment Variables

- `SCHOLAR_COOKIE_FILE`: Path to cookie file for session persistence
- `PYTHONPATH`: Set to project root for imports

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `pytest`
5. Run quality checks: `pre-commit run --all-files`
6. Commit your changes: `git commit -m "Description"`
7. Push to your fork: `git push origin feature-name`
8. Create a Pull Request

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure you're in the virtual environment and dependencies are installed
2. **Test failures**: Check that BeautifulSoup4 is installed: `pip install beautifulsoup4`
3. **Docker issues**: Ensure Docker daemon is running and you have sufficient disk space
4. **Rate limiting**: Use cookie persistence for higher query rates

### Getting Help

- Check the [README.md](README.md) for usage examples
- Run `python scholar.py --help` for command-line options
- Review test files for API usage examples
