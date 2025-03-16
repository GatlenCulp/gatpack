#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = gatpack
PYTHON_VERSION = 3.12
PYTHON_INTERPRETER = python
DOCS_PORT ?= 8000

# .PHONY: w-example
# example: ## Run example code
# 	weasyprint ./example/report.html ./example/test.pdf

# .PHONY: w-compile
# compile: ## Run compilation code
	# weasyprint ./user/02_web/cover.html ./user/03_pdf/cover-test.pdf

.PHONY: build
build: clean ## Builds the python project into a binary with pyinstaller.
	pyinstaller gatpack/main.py \
	--name GatPack \
	--add-data "$(shell python -c 'import cookiecutter; from pathlib import Path; print(Path(cookiecutter.__file__).parent/"VERSION.txt")')":cookiecutter/ \
	--icon=docs/images/icon.icns \
	--console \

.PHONY: docker-recording-studio
docker-recording-studio: ## Build and run the recording-studio Docker container
	docker build -t gatpack-recording-studio -f docker/recording-studio.Dockerfile .
	docker run -it --rm -v $(PWD):/app gatpack-recording-studio

.PHONY: gatpack
gatpack: ## Run gatpack cli
	echo "HELLO"

.PHONY: schema
schema: ## Generate GatPackCompose JSON schema
	python ./gatpack/schema/generate_json_schema.py

.PHONY: test-root
test-root: ## Tests the gatpack root functionality (infer)
	gatpack --from ./tests/root/test-tex-jinja.jinja.tex \
	-o ./tests/root/test-tex-jinja.tex

.PHONY: test-init
test-init: ## Run gatpack init
	cookiecutter "https://github.com/GatlenCulp/cookiecutter-gatpack" --checkout "dev"

.PHONY: test-render
test-render: ## Run gatpack render
	# gatpack render ./tests/test.jinja.tex ./tests/test.tex
	# rm ./user/01_templates/cover-test.tex
	# Test Standard Jinja Rendering
	cd ./tests/render && rm -f test-standard-jinja.tex && \
		gatpack render test-standard-jinja.jinja.tex \
		test-standard-jinja.tex \
		compose.gatpack.json
	# Test Special Jinja Rendering
	cd ./tests/render && rm -f test-tex-jinja.tex && \
		gatpack render test-tex-jinja.jinja.tex \
		test-tex-jinja.tex compose.gatpack.json \
		--no-use-standard-jinja

.PHONY: test-combine
test-combine: ## Run gatpack render
	# rm ./user/01_templates/cover-test.tex
	# gatpack combine ./tests/test.pdf ./tests/test.pdf ./tests/test-combine.pdf
	gatpack combine ./tests/combine/glob/test-*.pdf ./tests/combine/glob/test-glob-combine.pdf

.PHONY: test-build
test-build: ## Run gatpack build
	# rm ./user/01_templates/cover-test.tex
	gatpack build ./tests/test.tex ./tests/test-build.pdf
	# cd tests && pdflatex test-build.tex -interaction=nonstopmode -halt-on-error

.PHONY: test-footer
test-footer: ## Run gatpack footer
	# gatpack footer ./tests/footer/test-no-footer.pdf "Page n of N" ./tests/footer/test-footer.pdf
	gatpack footer ./tests/footer/test-no-footer.pdf ./tests/footer/test-footer.pdf --text '{n} of {N}' --overwrite

.PHONY: test-infer
test-infer: ## Run gatpack infer
	rm -f ./tests/infer/test.tex
	gatpack infer --overwrite \
	./tests/infer/test.jinja.tex \
	./tests/infer/test.pdf

.PHONY: test-root
test-root: ## Run gatpack with no subcommand (ie: infer)
	rm -f ./tests/infer/test.tex
	gatpack --overwrite \
	--from ./tests/infer/test.jinja.tex \
	--to ./tests/infer/test.pdf

#################################################################################
# UTILITIES                                                                     #
#################################################################################

_prep: ## Clean up .DS_Store files
	rm -f **/*/.DS_store

_welcome: ## Print a Welcome screen
	curl -s https://raw.githubusercontent.com/GatlenCulp/gatlens-opinionated-template/vscode-customization/welcome.txt

#################################################################################
# PACKAGE COMMANDS                                                              #
#################################################################################

.PHONY: create_environment
create_environment: ## Set up python interpreter environment
	uv venv
	@echo ">>> New virtualenv with uv created. Activate with:\nsource '.venv/bin/activate'"



.PHONY: requirements
requirements: ## Install Python Dep
	
	uv sync
	


.PHONY: publish-all
publish-all: format lint publish docs-publish ## Run format, lint, publish package and docs

#################################################################################
# CLEAN COMMANDS                                                                #
#################################################################################


.PHONY: clean
clean: ## Delete all compiled Python files
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


.PHONY: lint ## Lint using ruff (use `make format` to do formatting)
lint:
	ruff check --config pyproject.toml gatpack


.PHONY: format ## Format source code with black
format:
	ruff --config pyproject.toml gatpack

#################################################################################
# DOCS COMMANDS                                                                 #
#################################################################################

# Switched to using uv
docs-serve: ## Serve documentation locally on port $(DOCS_PORT)
	cd docs && \
	mkdocs serve -a localhost:$(DOCS_PORT) || \
	echo "\n\nInstance found running on $(DOCS_PORT), try killing process and rerun."

# Makes sure docs can be served prior to actually deploying
docs-publish: ## Build and deploy documentation to GitHub Pages
	cd docs && \
	mkdocs build && \
	mkdocs gh-deploy --clean

#################################################################################
# DATA COMMANDS                                                                 #
#################################################################################

#################################################################################
# TEST COMMANDS                                                                 #
#################################################################################

.PHONY: test
test: _prep ## Run all tests
	pytest -vvv --durations=0

.PHONY: test-fastest
test-fastest: _prep ## Run tests with fail-fast option
	pytest -vvv -FFF

# Requires pytest-watcher (Continuous Testing for Fast Tests)
.PHONY: test-continuous
test-continuous: _prep ## Run tests in watch mode using pytest-watcher
	ptw . --now --runner pytest --config-file pyproject.toml -vvv -FFF

.PHONY: test-debug-last
test-debug-last: ## Debug last failed test with pdb
	pytest --lf --pdb

.PHONY: _clean_manual_test
_clean_manual_test:
	rm -rf manual_test

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

.PHONY: data ## Make Dataset
data: requirements
	$(PYTHON_INTERPRETER) gatpack/dataset.py

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################


.PHONY: _print-logo
_print-logo: ## Prints the GOTem logo
	@echo "\033[38;5;39m   ____  ___ _____"
	@echo "  / ___|/ _ \_   _|__ _ __ ___"
	@echo " | |  _| | | || |/ _ \ '_ \` _ \\"
	@echo " | |_| | |_| || |  __/ | | | | |"
	@echo "  \____|\___/ |_|\___|_| |_| |_|\033[0m"


.PHONY: help
help: _print-logo  ## Show this help message
	@echo "\n\033[1m~ Available rules: ~\033[0m\n"
	@echo "For VSCode/Cursor, try: ⇧ ⌘ P, Tasks: Run Task\n"
	@grep -E '^[a-zA-Z][a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[38;5;222m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: all
all: help

.DEFAULT_GOAL := all
