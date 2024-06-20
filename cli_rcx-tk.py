# CLI for processing the metadata files

from pathlib import Path
import click
import os
import pandas as pd

def read_file(file_path: str) -> pd.DataFrame:
    file_extension = os.path.splitext(Path(file_path))[1].lower()
    if file_extension == '.csv':
        return pd.read_csv(Path(file_path), encoding='UTF-8')
    elif file_extension in ['.xls', '.xlsx']:
        return pd.read_excel(Path(file_path))
    elif file_extension in ['.tsv', '.txt']: 
        return pd.read_csv(Path(file_path), sep='\t')
    else:
        raise ValueError("Unsupported file format. Please provide a CSV, Excel, or TSV file.")

def save_dataframe_as_tsv(df: pd.DataFrame, file_path: str) -> None:
    if os.path.splitext(Path(file_path))[1] != ".tsv":
        raise ValueError("Unsupported file format. Please point to a TSV file.")
    df.to_csv(Path(file_path), sep='\t', index=False)
    
    
@click.command()
@click.argument('file_path')
@click.argument('out_path')
    
def process_metadata_file(file_path: str, out_path: str) -> None:
    columns_to_keep = {
        'File name': 'sampleName',
        'Type': 'sampleType',
        'Class ID': 'class',
        'Batch': 'batch',
        'Analytical order': 'injectionOrder'
    }

    df = read_file(Path(file_path))
    df = df[list(columns_to_keep.keys())].rename(columns=columns_to_keep)
    df['sampleName'] = df['sampleName'].str.replace(' ', '_')
    save_dataframe_as_tsv(df, Path(out_path))
    click.echo("Done!")

if __name__ == "__main__":
    process_metadata_file()