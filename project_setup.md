# Project Setup

Here we provide some details about the project setup. Most of the choices are explained in the
[guide](https://guide.esciencecenter.nl). Links to the relevant sections are included below. Feel free to remove this
text when the development of the software package takes off.

For a quick reference on software development, we refer to [the software guide
checklist](https://guide.esciencecenter.nl/#/best_practices/checklist).

## Python versions

This repository is set up with Python versions:

- 3.11
- 3.12

Add or remove Python versions based on project requirements. See [the
guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python) for more information about Python
versions.

## Package management and dependencies

For installing the dependencies and package management, [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) and [poetry](https://python-poetry.org/) have been used.

The dependencies are listed in the `pyproject.toml` file under the section `[tool.poetry.dependencies]` and `[tool.poetry.group.dev.dependencies]`.

## Packaging/One command install

To create a new environment, use the micromamba:

```console
micromamba create -n rcx-tk poetry
micromamba activate rcx-tk
```
To install all dependencies specified in the `pyproject.toml` file, use poetry:

```console
poetry install
```

## Testing and code coverage

- Tests should be put in the `tests` folder.
- The `tests` folder contains:
  - Example tests that you should replace with your own meaningful tests (file: `test_my_module.py`)
- The testing framework used is [PyTest](https://pytest.org)
  - [PyTest introduction](https://pythontest.com/pytest-book/)
  - PyTest is listed as a development dependency
  - This is configured in `pyproject.toml`
- The project uses [GitHub action workflows](https://docs.github.com/en/actions) to automatically run tests on GitHub infrastructure against multiple Python versions
  - Workflows can be found in [`.github/workflows`](.github/workflows/)
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=testing)

## Documentation

- Documentation should be put in the [`docs/`](docs/) directory. The contents have been generated using `sphinx-quickstart` (Sphinx version 1.6.5).
- We recommend writing the documentation using Restructured Text (reST) and Google style docstrings.
  - [Restructured Text (reST) and Sphinx CheatSheet](https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html)
  - [Google style docstring examples](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
- The documentation is set up with the ReadTheDocs Sphinx theme.
  - Check out its [configuration options](https://sphinx-rtd-theme.readthedocs.io/en/latest/).
- [AutoAPI](https://sphinx-autoapi.readthedocs.io/) is used to generate documentation for the package Python objects.
- `.readthedocs.yaml` is the ReadTheDocs configuration file. When ReadTheDocs is building the documentation this package and its development dependencies are installed so the API reference can be rendered.
- [Relevant section in the guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=writingdocumentation)

## Coding style conventions and code quality

- [Relevant section in the NLeSC guide](https://guide.esciencecenter.nl/#/best_practices/language_guides/python?id=coding-style-conventions) and [README.dev.md](README.dev.md).

## Continuous code quality

[Sonarcloud](https://sonarcloud.io/) is used to perform quality analysis and code coverage report

- `sonar-project.properties` is the SonarCloud [configuration](https://docs.sonarqube.org/latest/analysis/analysis-parameters/) file
- `.github/workflows/sonarcloud.yml` is the GitHub action workflow which performs the SonarCloud analysis

## Package version number

- Releases are labelled using the [semantic versioning](https://guide.esciencecenter.nl/#/best_practices/releases?id=semantic-versioning).

## CHANGELOG.md

- To document the changes, we use the [CHANGELOG.md](https://github.com/RECETOX/rcx-tk/blob/master/CHANGELOG.md)
