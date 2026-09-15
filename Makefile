.PHONY: test

PYTHON ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python)

test:
	$(PYTHON) -m pytest
