import click
from rcx_tk.alkanes import process_alkane_file
from rcx_tk.msdial import process_msdial_file
from rcx_tk.sequence import process_sequence_file


@click.group()
def main():
    """rcx_tk command-line interface."""


@main.command("sequence")
@click.argument("file_path")
@click.argument("out_path")
def sequence(file_path: str, out_path: str) -> None:
    """Process a sequence metadata file."""
    process_sequence_file(file_path, out_path)


@main.command("alkanes")
@click.argument("file_path")
@click.argument("out_path")
def alkanes(file_path: str, out_path: str) -> None:
    """Process an alkane file."""
    process_alkane_file(file_path, out_path)


@main.command("msdial")
@click.argument("file_path")
@click.argument("out_path")
@click.argument("mz_tol_ppm", required=False, default=5, type=int)
def msdial(file_path: str, out_path: str, mz_tol_ppm: int) -> None:
    """Process an MSDIAL output file."""
    process_msdial_file(file_path, out_path, mz_tol_ppm)


if __name__ == "__main__":
    main()
