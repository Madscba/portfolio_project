"""Test file."""

import pandas as pd


def load_file(file_name: str):
    """Load file with pandas.

    Args:
        file_name:

    Returns:
        file: loaded_file
    """
    file_type = str(file_name).split(".")[-1]

    if file_type == 'parquet':
        file = pd.read_parquet(file_name)
    elif file_type == 'csv':
        file = pd.read_csv(file_name)
    elif file_type == 'xlsm':
        file = pd.read_excel(file_name)
    elif file_type in ['picke', 'pkl']:
        file = pd.read_pickle(file_name)
    else:
        raise Exception(f"File type {file_type} not implemented yet")

    return file
