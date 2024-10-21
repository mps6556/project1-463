# data_handler.py

import pandas as pd

def load_data(file_path):
    # read into a df
    return pd.read_csv(file_path)

def preprocess_data(df, date_column):
    # convert date column to datetime
    df[date_column] = pd.to_datetime(df[date_column])

    # sort by date
    df = df.sort_values(by=date_column)
    return df
