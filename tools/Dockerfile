FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install .[dev,charts]
CMD pylint penchmark && mypy penchmark && pytest --disable-pytest-warnings --cov=penchmark penchmark/tests
