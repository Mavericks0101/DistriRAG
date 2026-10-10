.PHONY: install test lint format clean run

install:
	python -m pip install --upgrade pip
	pip install -e ".[dev]"

test:
	pytest -v

lint:
	black --check src tests
	isort --check-only src tests

format:
	black src tests
	isort src tests

run:
	uvicorn distrirag.api.main:app --reload --host 0.0.0.0 --port 8000

clean:
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf *.egg-info
