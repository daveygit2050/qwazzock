.EXPORT_ALL_VARIABLES:
version := $(shell poetry version | awk '{print $$2}')

.PHONY: bandit
bandit: bandit
	poetry run bandit -r ./ --exclude ./tests

.PHONY: black
black:
	poetry run black qwazzock/ tests/

.PHONY: build
build: build_wheel build_image
	@echo Build complete.

.PHONY: build_image
build_image:
	docker build --build-arg version=${version} --tag qwazzock:latest --tag qwazzock:${version} .

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
	export FLASK_ENV=development && export PYTHONPATH="${PYTHONPATH}:`pwd`/" && poetry run python qwazzock/__init__.py

.PHONY: init
init:
	pip install poetry --upgrade
	poetry install
	poetry run pre-commit install

.PHONY: release
release: build
	git update-index --refresh 
	git diff-index --quiet HEAD --
	git tag --sign --message "qwazzock version ${version}" ${version} && git push --tags

.PHONY: run
run:
	docker run -d -p 5000:5000 qwazzock:${version}

.PHONY: safety
safety:
	poetry run safety check

.PHONY: test
test: unit_test bandit safety
	@echo Tests complete.

.PHONY: unit_test
unit_test: black
	export PYTHONPATH="${PYTHONPATH}:`pwd`/" && poetry run pytest --ignore ./tests/component
