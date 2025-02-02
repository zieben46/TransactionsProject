.PHONY: test package deploy

tests: pre-commit
	python -m unittest

ut:
	python -m unittest

pre-commit:
	pre-commit run --all-files

static-check:
	mypy --explicit-package-bases .




test:
	python -m unittest discover -s backend_package/tests -p "test_*.py"

package:
	cd backend_package && python setup.py sdist

deploy:
	pip install backend_package/dist/streamlit_crud_backend-0.1.0.tar.gz
	cd streamlit_app && streamlit run app.py