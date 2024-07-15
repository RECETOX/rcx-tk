## Badges

| fair-software.eu recommendations | |
| :-- | :--  |
| (1/5) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/RECETOX/rcx-tk) |
| (2/5) license                      | [![github license badge](https://img.shields.io/github/license/RECETOX/rcx-tk)](https://github.com/RECETOX/rcx-tk) |
| (3/4) citation                     | [![DOI](https://zenodo.org/badge/DOI/<replace-with-created-DOI>.svg)](https://doi.org/<replace-with-created-DOI>) |
| (4/4) checklist                    | [![workflow cii badge](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>/badge)](https://bestpractices.coreinfrastructure.org/projects/<replace-with-created-project-identifier>) |
| howfairis                          | [![fair-software badge](https://img.shields.io/badge/fair--software.eu-%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8F%20%20%E2%97%8B-yellow)](https://fair-software.eu) |
| **Other best practices**           | &nbsp; |
| Static analysis                    | [![workflow scq badge](https://sonarcloud.io/api/project_badges/measure?project=RECETOX_rcx-tk&metric=alert_status)](https://sonarcloud.io/dashboard?id=RECETOX_rcx-tk) |
| Coverage                           | [![workflow scc badge](https://sonarcloud.io/api/project_badges/measure?project=RECETOX_rcx-tk&metric=coverage)](https://sonarcloud.io/dashboard?id=RECETOX_rcx-tk) |
| Documentation                      | [![Documentation Status](https://readthedocs.org/projects/rcx-tk/badge/?version=latest)](https://rcx-tk.readthedocs.io/en/latest/?badge=latest) |
| **GitHub Actions**                 | &nbsp; |
| Build                              | [![build](https://github.com/RECETOX/rcx-tk/actions/workflows/build.yml/badge.svg)](https://github.com/RECETOX/rcx-tk/actions/workflows/build.yml) |
| Citation data consistency          | [![cffconvert](https://github.com/RECETOX/rcx-tk/actions/workflows/cffconvert.yml/badge.svg)](https://github.com/RECETOX/rcx-tk/actions/workflows/cffconvert.yml) |
| SonarCloud                         | [![sonarcloud](https://github.com/RECETOX/rcx-tk/actions/workflows/sonarcloud.yml/badge.svg)](https://github.com/RECETOX/rcx-tk/actions/workflows/sonarcloud.yml) |
| MarkDown link checker              | [![markdown-link-check](https://github.com/RECETOX/rcx-tk/actions/workflows/markdown-link-check.yml/badge.svg)](https://github.com/RECETOX/rcx-tk/actions/workflows/markdown-link-check.yml) |

## How to use rcx_tk

`rcx-tk` package provides tools to process the metadata or alkane files.

On the input, the user is expected to supply a path to the metadata/alkane file in tsv/csv/xls/xlsx file. The file is then converted to a dataframe which is further processed. The main steps are:

- columns rearrangement
- validation of the file names
- validation that the `injectionNumber` column is of integer type
- derivation of new metadata: `sampleName`, `sequenceIdentifier`, `sampleIdentifier` and `localOrder`

Finally, the processed dataframe is saved into user-defined location.

## Installation

To install rcx_tk from GitHub repository, do:

```console
git clone git@github.com:RECETOX/rcx-tk.git
cd rcx-tk
poetry install
```

The main functions are process_metadata_file and process_alkane_ri_file.

The tool can be run also using command-line interface, either by the python3 or poetry:

```console
python3 <path-to-__main.py__> --method='' <path-to-input-data> <path-to-output-data>
```

```console
poetry run rcx_tk --method='' <file-path-to-input-data> <file-path-to-output-data>
```
## Documentation

The project is documented [here](https://rcx-tk.readthedocs.io/en/latest/?badge=latest).

## Contributing

If you want to contribute to the development of rcx_tk,
have a look at the [contribution guidelines](CONTRIBUTING.md).

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
