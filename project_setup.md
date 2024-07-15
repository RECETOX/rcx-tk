# Project Setup

## Python versions

This repository is set up with Python versions:

- 3.11
- 3.12

## Package management and dependencies

For installing the dependencies and package management, [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) and [poetry](https://python-poetry.org/) have been used.

The dependencies are listed in the `pyproject.toml` file under the section `[tool.poetry.dependencies]` and `[tool.poetry.group.dev.dependencies]`.

## Packaging/One command install

To create a new environment, use the micromamba:

```console
micromamba create rcx-tk
micromamba activate rcx-tk
```
To install all dependencies specified in the `pyproject.toml` file, use poetry:

```console
poetry install
```

## Testing and code coverage

- Tests are in the `tests` folder, in the `test_process_metadata_file.py` file.
- The testing framework used is [PyTest](https://pytest.org)
- The project uses [GitHub action workflows](https://docs.github.com/en/actions) to automatically run tests on GitHub infrastructure against multiple Python versions

## Documentation

- Documentation is in the [`docs/`](docs/) directory. The contents have been generated using `sphinx-quickstart` (Sphinx version 1.6.5).
- The documentation is set up with the ReadTheDocs Sphinx theme.
- [AutoAPI](https://sphinx-autoapi.readthedocs.io/) is used to generate documentation for the package Python objects.
- `.readthedocs.yaml` is the ReadTheDocs configuration file. When ReadTheDocs is building the documentation this package and its development dependencies are installed so the API reference can be rendered.

## Continuous code quality

[Sonarcloud](https://sonarcloud.io/) is used to perform quality analysis and code coverage report

- `sonar-project.properties` is the SonarCloud [configuration](https://docs.sonarqube.org/latest/analysis/analysis-parameters/) file
- `.github/workflows/sonarcloud.yml` is the GitHub action workflow which performs the SonarCloud analysis

## Package version number

- Releases are labelled using the [semantic versioning](https://guide.esciencecenter.nl/#/best_practices/releases?id=semantic-versioning).

## CHANGELOG.md

- To document the changes, we use the [CHANGELOG.md](https://github.com/RECETOX/rcx-tk/blob/master/CHANGELOG.md)
