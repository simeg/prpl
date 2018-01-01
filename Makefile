.PHONY: ci install lint test

ci: install lint test

install:
	pip install -r requirements.txt

lint:
	pep8 --format=pylint --verbose src prpl test

test:
	pushd test; pytest tests.py; popd
