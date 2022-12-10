.PHONY: create-venv pip-compile pip-install run-sample

create-venv:
	python -m venv .venv
pip-compile:
	pip install -U pip pip-tools
	pip-compile -U --resolver=backtracking
pip-install:
	pip install -U pip
	pip install -U -r ./requirements-dev.in
	test -f ./requirements.txt && pip install -U -r ./requirements.txt || :
run-sample:
	python -m papical ./sample.csv
