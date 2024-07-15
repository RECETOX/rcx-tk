# `rcx_tk` developer documentation

If you're looking for user documentation, go [here](README.md).

## Package installation

To create a new environment, use the micromamba:

```console
micromamba create -n rcx-tk poetry
micromamba activate rcx-tk
```
To install all dependencies specified in the `pyproject.toml` file, use poetry:

```console
poetry install
```

A command line interface was also implemented using Click, so the package can be run by either using python3:

```console
python3 <path-to-__main.py__> --method='' <path-to-input-data> <path-to-output-data>
```

or using poetry:

```console
poetry run rcx_tk --method='' <file-path-to-input-data> <file-path-to-output-data>
```

## Running the tests

There are two ways to run tests.

The first way requires an activated virtual environment with the development tools installed:

```shell
pytest -v
```

The second is to use `tox`, which can be installed separately (e.g. with `pip install tox`), i.e. not necessarily inside the virtual environment you use for installing `rcx_tk`, but then builds the necessary virtual environments itself by simply running:

```shell
tox
```

Testing with `tox` allows for keeping the testing environment separate from your development environment.
The development environment will typically accumulate (old) packages during development that interfere with testing; this problem is avoided by testing with `tox`.

### Test coverage

In addition to just running the tests to see if they pass, they can be used for coverage statistics, i.e. to determine how much of the package's code is actually executed during tests.
In an activated virtual environment with the development tools installed, inside the package directory, run:

```shell
coverage run
```

This runs tests and stores the result in a `.coverage` file.
To see the results on the command line, run

```shell
coverage report
```

`coverage` can also generate output in HTML and other formats; see `coverage help` for more information.

## Running linters locally

For linting and sorting imports we will use [ruff](https://beta.ruff.rs/docs/). Running the linters requires an 
activated virtual environment with the development tools installed.

```shell
# linter
ruff .

# linter with automatic fixing
ruff . --fix
```

To fix readability of your code style you can use [yapf](https://github.com/google/yapf).

You can enable automatic linting with `ruff` on commit by enabling the git hook from `.githooks/pre-commit`, like so:

```shell
git config --local core.hooksPath .githooks
```

## Generating the API docs

```shell
cd docs
make html
```

The documentation will be in `docs/_build/html`

If you do not have `make` use

```shell
sphinx-build -b html docs docs/_build/html
```

To find undocumented Python objects run

```shell
cd docs
make coverage
cat _build/coverage/python.txt
```

To [test snippets](https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html) in documentation run

```shell
cd docs
make doctest
```

## Versioning

Bumping the version across all files is done with [bump-my-version](https://github.com/callowayproject/bump-my-version), e.g.

```shell
poetry version major  # bumps from e.g. 0.3.2 to 1.0.0
poetry version minor  # bumps from e.g. 0.3.2 to 0.4.0
poetry version patch  # bumps from e.g. 0.3.2 to 0.3.3
```

## Making a release

This section describes how to make a release in 3 parts:

1. preparation
1. making a release on PyPI
1. making a release on GitHub

### (1/3) Preparation

1. Update the <CHANGELOG.md> (don't forget to update links at bottom of page)
2. Verify that the information in [`CITATION.cff`](CITATION.cff) is correct.
3. Make sure the [version has been updated](#versioning).
4. Run the unit tests with `pytest -v`

### (2/3) PyPI

In a new terminal:

```shell
# OPTIONAL: prepare a new directory with fresh git clone to ensure the release
# has the state of origin/main branch
cd $(mktemp -d rcx_tk.XXXXXX)
git clone git@github.com:RECETOX/rcx-tk .
```

Create and activate a new environment:

```console
micromamba create rcx-tk-pypi
micromamba activate rcx-tk-pypi
```

Create an account on PypI.

In the Account settings, find the API tokens section and click on "Add API token". Copy your token.

Add your API token to Poetry:

```console
poetry config pypi-token.pypi your-api-token
```

Build your project:

```console
poetry build
```

Publish your package to PyPI:

```console
poetry publish
```

### (3/3) GitHub

Don't forget to also make a [release on GitHub](https://github.com/RECETOX/rcx-tk/releases/new). If your repository uses the GitHub-Zenodo integration this will also trigger Zenodo into making a snapshot of your repository and sticking a DOI on it.