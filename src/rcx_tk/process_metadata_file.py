import pandas as pd
import os

def read_file(file_path):
    """Reads a file and returns a DataFrame based on the file extension."""
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.csv':
        return pd.read_csv(file_path, encoding='UTF-8')
    elif file_extension in ['.xls', '.xlsx']:
        return pd.read_excel(file_path)
    elif file_extension == '.txt':
        return pd.read_csv(file_path, sep='\t')
    else:
        raise ValueError("Unsupported file format. Please provide a CSV, Excel, or TSV file.")

def save_dataframe_as_tsv(df, file_path):
    """Saves a DataFrame as a TSV file."""
    if os.path.splitext(file_path)[1] != ".tsv":
        raise ValueError("Unsupported file format. Please point to a TSV file.")
    df.to_csv(file_path, sep='\t', index=False)
    

def process_metadata_file(file_path, out_path):
    """Processes a metadata file, keeping and renaming specific columns."""
    columns_to_keep = {
        'File name': 'sampleName',
        'Type': 'sampleType',
        'Class ID': 'class',
        'Batch': 'batch',
        'Analytical order': 'injectionOrder'
    }
    
    df = read_file(file_path)
    df = df[list(columns_to_keep.keys())].rename(columns=columns_to_keep)
    df['sampleName'] = df['sampleName'].str.replace(' ', '_')
    save_dataframe_as_tsv(df, out_path)

def process_alkane_ri_file(file_path, out_path):
    """Processes an Alkane RI file, keeping and renaming specific columns."""
    columns_to_keep = {
        'Carbon number': 'carbon_number',
        'RT (min)': 'rt'
    }
    
    df = read_file(file_path)
    df.columns = df.columns.str.strip()
    df = df.rename(columns=columns_to_keep)
    save_dataframe_as_tsv(df, out_path)

