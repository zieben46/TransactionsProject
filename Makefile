tests: pre-commit
	python -m unittest

ut:
	python -m unittest

pre-commit:
	pre-commit run --all-files

static-check:
	mypy --explicit-package-bases .

