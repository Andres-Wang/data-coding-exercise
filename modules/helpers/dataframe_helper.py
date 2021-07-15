import pandas as pd


def read_local_file_to_df(file_path: str, file_format: str, chunk_size: int = None):
    """
    Reads a local file to df
    :param chunk_size: Max size of rows for every chunk
    :return: pd.Dataframe if chunk_size is not provided, TextFileReader if chunk_size provided
    """
    if file_format == 'CSV':
        return pd.read_csv(file_path, chunksize=chunk_size)
    if file_format == 'LINE_DELIMITED_JSON':
        return pd.read_json(file_path, chunksize=chunk_size, lines=True)
    else:
        raise RuntimeError(f"Invalid file format: {file_format}. ")


def one_to_one_mappings_from_df(df: pd.DataFrame, index_col: str, value_col: str) -> dict:
    """
    Generates a one to one mapping between two columns, this should only be used when index_col is a unique key
    :return: A dict with the mappings
    """
    mapping = dict()
    for _, row in df.iterrows():
        if row[index_col] in mapping:
            raise ValueError(f"{index_col} field contains duplicate value.")
        mapping[row[index_col]] = row[value_col]
    return mapping


def filter_df_by_timestamp(df: pd.DataFrame, timestamp_col: str, start_ts: str, end_ts: str) -> pd.DataFrame:
    """
    Returns the filtered dataframe, given the start and end timestamp
    :param start_ts: Inclusive
    :param end_ts: Exclusive
    """
    return df[(df[timestamp_col] >= start_ts) & (df[timestamp_col] < end_ts)]
