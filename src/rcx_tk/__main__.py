import click
from rcx_tk.alkanes import process_alkane_file
from rcx_tk.msdial import process_msdial_file
from rcx_tk.sequence import process_sequence_file


@click.command()
@click.option(
    "--method",
    type=click.Choice(["sequence", "alkanes", "msdial"]),
    required=True,
    help="A file type to be processed, either sequence or alkanes file.",
)
@click.argument("file_path")
@click.argument("out_path")
def main(method, file_path, out_path):
    """Process sequence or alkane file.

    Args:
        method (string): Whether a sequence or alkane file should be processed.
        file_path (path): A path to the input data.
        out_path (path): A path where the processed data will be exported to.
    """
    if method == "sequence":
        process_sequence_file(file_path, out_path)
    elif method == "alkanes":
        process_alkane_file(file_path, out_path)
    elif method == "msdial":
        process_msdial_file(file_path, out_path)


if __name__ == "__main__":
    main()
