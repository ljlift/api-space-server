.PHONY: init run

# init python virtual environment
init:
	PIPENV_VENV_IN_PROJECT=1 pipenv install

run:
	PYTHONPATH=. python -m app.main