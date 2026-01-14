import pandas as pd

def read_file(FILENAME, header):
    """
    :param FILENAME: The file
    :param header: adding a header to a file for raw data
    :return: a df of the file using pandas
    """
    df = pd.read_csv(FILENAME)
    df.loc[-1] = df.columns
    df.index = df.index + 1
    df = df.sort_index().reset_index(drop=True)
    df.columns = header
    return df