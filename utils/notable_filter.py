
import pandas as pd

class NotableFilter:
    def __init__(self, notable_list):
        self.notable_list = notable_list

    def filter(self, df):
        return df[df['Name'].isin(self.notable_list)]

    def filter_file(self, file_path):
        file_extension = file_path.split('.')[-1]
        if file_extension in ['xls', 'xlsx']:
            df = pd.read_excel(file_path)
        elif file_extension == 'csv':
            df = pd.read_csv(file_path)
        else:
            raise ValueError(f'Unsupported file extension: {file_extension}')

        return self.filter(df)
