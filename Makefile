.PHONY: create-venv pip-compile pip-install

create-venv:
	python -m venv .venv
pip-compile:
	pip-compile -U
pip-install:
	./.venv/bin/pip install -U pip
	./.venv/bin/pip install -U -r ./requirements-dev.in
	test -f ./requirements.txt && ./.venv/bin/pip install -U -r ./requirements.txt || :
