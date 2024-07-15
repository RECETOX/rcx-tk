# `rcx_tk` developer documentation

If you're looking for user documentation, go [here](README.md).

## Package installation

To create a new environment, use the micromamba:

```console
micromamba create rcx-tk
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

Tests were written using the pytest package and can be run as:

```shell
pytest .
```
