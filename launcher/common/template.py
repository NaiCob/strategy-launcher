import os
from typing import Any

import pandas as pd


def common_function(message: str) -> None:
    print(message)
    return None


def get_path_to_file(path_to_folder: str, file_name: str, file_extension: str):
    return os.path.abspath(f"{path_to_folder}/{file_name}.{file_extension}")


def read_xlsx_file(path: str, row: int, sheet_name: str) -> pd.DataFrame:
    df = pd.read_excel(path, dtype=str, skiprows=row, sheet_name=sheet_name)
    df.columns = df.columns.str.rstrip()
    return df


def add_standard_column(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    for col in columns:
        if col not in df.columns:
            df[col] = None
    
    return df


def add_constant_column(df: pd.DataFrame, column_name: str, const_value: Any) -> pd.DataFrame:
    df.drop(columns=[column_name])
    df[column_name] = const_value
    return df


def clean_nip_number(df: pd.DataFrame, nip_column_name: str) -> pd.DataFrame:
    df[nip_column_name] = df[nip_column_name].str.replace("-", "").str.replace("PL", "")
    return df


def save_as_csv(df: pd.DataFrame, path: str) -> None:
    df.to_csv(path, header=True, sep=';', encoding='cp1250', index=False)
