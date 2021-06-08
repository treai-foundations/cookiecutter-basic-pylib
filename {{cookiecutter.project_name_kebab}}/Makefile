.PHONY: clean clean-test clean-pyc clean-build lint test coverage format help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint:  ## use the default linter pylint and the optional flake8 to verify the code style
{%- if cookiecutter.use_flake8 == 'y' %}
	flake8 {{ cookiecutter.project_name_snake }} tests
{%- endif %}
	pylint {{ cookiecutter.project_name_snake }} tests setup.py

test: ## run tests quickly with the default Python
	pytest

{%- if cookiecutter.use_coverage == 'y' %}
coverage: ## check code coverage quickly with the default Python
	coverage run --source {{ cookiecutter.project_name_snake }} -m pytest
	coverage report -m --omit={{ cookiecutter.project_name_snake }}/_version.py
	coverage html

coverage-web: coverage ## check code coverage and open report in web browser
	$(BROWSER) htmlcov/index.html
{%- endif %}

format: ## format the code using black and the line-length set to 100
	black --line-length 100 {{ cookiecutter.project_name_snake }} tests setup.py

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
