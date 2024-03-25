# take-home-test-starter

## Creating a development environment

This repository uses [poetry](https://python-poetry.org/) and Python 3.10. Follow poetry's [installation instructions](https://python-poetry.org/docs/#installing-with-the-official-installer) to get set up.

We recommend using [pyenv](https://github.com/pyenv/pyenv) to manage your Python version.

Project dependencies can be installed by calling:

```bash
poetry install
```

Activate the virtual environment using:

```bash
poetry shell
```

### Installing pre-commit hooks

There are [pre-commit](https://pre-commit.com/) hooks available to lint, format and sort the code.

To install the pre-commit hooks, run:

```bash
pre-commit install -c .pre-commit-config.yaml
```

Pre-commit hooks can be invoked manually using:

```bash
pre-commit run -c .pre-commit-config.yaml --all-files
```

## Running the code

```bash
python -m take_home_test_starter
```

## Running the tests

```bash
python -m pytest .
```

## Using the Docker image

The docker image, defined in the `Dockerfile` contains the setup needed for Poetry and GDAL.

```bash
docker build -t take-home-test-starter:latest .
```

You can then run the code in the image:

```console
docker run --rm -it take-home-test-starter:latest python -m take_home_test_starter
```

Or run the tests:

```console
docker run --rm -it take-home-test-starter:latest pytest
```

If you want to keep the source code up-to-date as you run, add `-v "$(pwd)/take_home_test_starter:/app/take_home_test_starter" -v "$(pwd)/tests:/app/tests"` to the `docker` arguments.
