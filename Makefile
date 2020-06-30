build:
	python setup.py sdist bdist_wheel

test:
	pytest --disable-pytest-warnings --cov=penchmark penchmark/tests

check:
	pylint penchmark && mypy penchmark

clean:
	rm -rf *.egg-info/ dist/ build/
