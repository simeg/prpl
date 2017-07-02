.PHONY: ci install lint test

python = /usr/bin/env python3

ci: install lint test

install:
	pip install -r requirements.txt

lint:
	pep8 --format=pylint . && pep8 --format=pylint prpl

test:
	python tests.py
