import click
from rcx_tk.alkanes import process_alkane_file
from rcx_tk.msdial import process_msdial_file
from rcx_tk.sequence import process_sequence_file


@click.group()
def main():
    """rcx_tk - Processing tool for metabolomics data and metadata.

    This tool provides subcommands for processing different types of metabolomics
    files: sequence metadata files, alkane retention index files, and MSDIAL
    output files.
    """


@main.command("sequence")
@click.argument("file_path", type=click.Path())
@click.argument("out_path", type=click.Path())
def sequence(file_path: str, out_path: str) -> None:
    """Process a sequence metadata file.

    Processes a sequence metadata file to perform the following operations:
    - Validate and rearrange columns
    - Validate file names
    - Ensure 'injectionOrder' column is of integer type
    - Derive new metadata columns: sampleName, sequenceIdentifier,
      subjectIdentifier, and localOrder

    The processed metadata is exported as a TSV file.

    Args:
        file_path: Path to the input metadata file.
        out_path: Path where the processed metadata will be saved.
    """
    process_sequence_file(file_path, out_path)


@main.command("alkanes")
@click.argument("file_path", type=click.Path())
@click.argument("out_path", type=click.Path())
def alkanes(file_path: str, out_path: str) -> None:
    """Process an alkane retention index file.

    Extracts and processes alkane retention index data from the input file,
    producing a structured output containing carbon numbers and retention times.
    The processed data is exported as a TSV file.

    Args:
        file_path: Path to the input alkane file.
        out_path: Path where the processed alkane data will be saved.
    """
    process_alkane_file(file_path, out_path)


@main.command("msdial")
@click.argument("file_path", type=click.Path())
@click.argument("out_path", type=click.Path())
@click.argument("mz_tol_ppm", required=False, default=5, type=int)
def msdial(file_path: str, out_path: str, mz_tol_ppm: int) -> None:
    """Process an MSDIAL output file to merge duplicate alignments.

    Features with identical peak abundances across samples are identified
    as duplicates and merged using aggregation:
    - Mean aggregation for RT, m/z, and other numeric metadata
    - Concatenation for text metadata
    - Maximum values for abundance data

    Args:
        file_path: Path to the input MSDIAL output file.
        out_path: Path where the processed MSDIAL data will be saved.
        mz_tol_ppm: Mass-to-charge tolerance in parts per million (PPM) used
            to distinguish between duplicate alignments. Lower values create
            finer groupings. Default is 5 PPM.
    """
    process_msdial_file(file_path, out_path, mz_tol_ppm)


if __name__ == "__main__":
    main()
