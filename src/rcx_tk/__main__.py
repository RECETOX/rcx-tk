import click

from rcx_tk.process_metadata_file import process_alkane_ri_file, process_metadata_file


@click.command()
@click.argument('method')
@click.argument('file_path')
@click.argument('out_path')
def main(method, file_path, out_path):
    """Process metadata or alkane file.

    Args:
        method (string): A type of the file which is provided: a metadata file or an alkane file.
        file_path (path): A path to the input data.
        out_path (path): A path where the processed data will be exported to.
    """
    if method == "metadata":
        process_metadata_file(file_path, out_path)
        click.echo("Metadata done!")
    elif method == "alkanes":
        process_alkane_ri_file(file_path, out_path)
        click.echo("Alkanes done!")


if __name__ == "__main__":
    main()