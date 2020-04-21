.EXPORT_ALL_VARIABLES:

.PHONY: black
black:
	poetry run black qwazzock/ tests/

.PHONY: dev
dev:
	export PYTHONPATH="${PYTHONPATH}:`pwd`/" && poetry run python qwazzock/__init__.py

.PHONY: test
test: black
	export PYTHONPATH="${PYTHONPATH}:`pwd`/" && poetry run pytest --ignore ./tests/component
