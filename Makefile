check:
	pylint penchmark && mypy penchmark

test:
	pytest --disable-pytest-warnings --cov=penchmark penchmark/tests

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf *.egg-info/ dist/ build/
