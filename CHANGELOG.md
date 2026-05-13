# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Changed
- changed join char for string cols in msdial method from , to ;

## [0.3.0] - 2026-04-30
### Changed
- changed behaviour in clustering for msdial that clusters are now refined and split based on mz tolerance [#48](https://github.com/RECETOX/rcx-tk/pull/48)
- updated dependencies [#48](https://github.com/RECETOX/rcx-tk/pull/48)
- updated cli to have multiple commands [#48](https://github.com/RECETOX/rcx-tk/pull/48)

## [0.2.2] - 2026-04-30
### Changed
- fixed bug in writing msdial corrected outputs where first skipped lines were not written properly. [#47](https://github.com/RECETOX/rcx-tk/pull/47)

## [0.2.1] - 2026-04-28
### Changed
- fixed bug in reading msdial files which was due to wring reading of the header in tabular format [#44](https://github.com/RECETOX/rcx-tk/pull/44)

## [0.1.0] - 2024-07-15

### Added

- function to read the metadata or alkane file in csv/tsv/xls/xlsx format
- function to process the metadata file: validate file names, derive and rearrange additional metadata columns
- function to save the processed metadata or alkane dataframe as tsv

### Removed

### Changed

[Unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v1.0.0...HEAD
[0.0.1]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/v0.0.1
