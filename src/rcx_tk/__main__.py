import click

from rcx_tk.process_metadata_file import process_alkane_ri_file, process_metadata_file


@click.command()
@click.option('--method', type=click.Choice(['metadata', 'alkanes']), required = True, help = 'A file type to be processed, either metadata or alkanes file.')
@click.argument('file_path')
@click.argument('out_path')
def main(method, file_path, out_path):
    """Process metadata or alkane file.

    Args:
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