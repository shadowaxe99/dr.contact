
import os
import pandas as pd
from typing import List

class FileHandler:
    SUPPORTED_EXTENSIONS = ['xls', 'xlsx', 'ods', 'csv', 'pdf', 'doc', 'docx', 'ppt', 'pptx', 'txt']

    @staticmethod
    def is_supported_file(file_path: str) -> bool:
        _, extension = os.path.splitext(file_path)
        return extension[1:] in FileHandler.SUPPORTED_EXTENSIONS

    @staticmethod
    def read_file(file_path: str) -> pd.DataFrame:
        if not FileHandler.is_supported_file(file_path):
            raise ValueError(f"Unsupported file type: {file_path}")

        _, extension = os.path.splitext(file_path)
        extension = extension[1:]

        if extension in ['xls', 'xlsx', 'ods', 'csv']:
            return pd.read_csv(file_path)
        elif extension in ['doc', 'docx', 'ppt', 'pptx', 'txt']:
            with open(file_path, 'r') as file:
                return pd.DataFrame(file.readlines())
        else:
            raise ValueError(f"Unsupported file type: {file_path}")

    @staticmethod
    def write_to_file(data: List[str], file_path: str):
        with open(file_path, 'w') as file:
            file.writelines(data)
