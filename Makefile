.PHONY: bandit
bandit: bandit
	poetry run bandit -r ./ --exclude ./tests

.PHONY: black
black:
	poetry run black qwazzock/ tests/

.PHONY: build_wheel build_image
build:
	@echo Build complete.

.PHONY: build_image
build_image:
	docker build --tag qwazzock:latest --tag qwazzock:$$(poetry version | awk '{print $$2}') .

.PHONY: build_wheel
build_wheel: test clean
	poetry build

.PHONY: clean
clean:
	rm -rf ./dist/
	rm -rf ./.mypy_cache
	rm -rf ./.pytest_cache
	rm -rf ./qwazzock.egg-info
	rm -f .coverage

.PHONY: dev
dev:
	export PYTHONPATH="${PYTHONPATH}:`pwd`/" && poetry run python qwazzock/__init__.py

.PHONY: init
init:
	pip install poetry --upgrade
	poetry install
	poetry run pre-commit install

.PHONY: safety
safety:
	poetry run safety check

.PHONY: test
test: unit_test bandit safety
	@echo Tests complete.

.PHONY: unit_test
unit_test: black
	export PYTHONPATH="${PYTHONPATH}:`pwd`/" && poetry run pytest --ignore ./tests/component
