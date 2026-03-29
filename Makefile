.PHONY: install dev-install test test-cov lint format check clean

install:
	pip install .

dev-install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=src --cov-report=term-missing

lint:
	ruff check .

format:
	ruff format .

check:
	ruff check . && ruff format --check .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	rm -rf .ruff_cache .pytest_cache .mypy_cache
