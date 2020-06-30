test:
	pytest --disable-pytest-warnings --cov=penchmark penchmark/tests

check:
	pylint penchmark && mypy penchmark
