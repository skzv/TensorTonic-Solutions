import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)

    values = df[column]

    result = {
        "values": values.tolist(),
        "length": values.size
    }

    return result