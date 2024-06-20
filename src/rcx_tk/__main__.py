import click

from rcx_tk.process_metadata_file import process_alkane_ri_file, process_metadata_file


@click.command()
@click.argument('method')
@click.argument('file_path')
@click.argument('out_path')
def main(method, file_path, out_path):
    if method == "metadata":
        process_metadata_file(file_path, out_path)
        click.echo("Metadata done!")
    elif method == "alkanes":
        process_alkane_ri_file(file_path, out_path)
        click.echo("Alkanes done!")


if __name__ == "__main__":
    main()