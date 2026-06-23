import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """

    df = pd.DataFrame(data)
    mask = df[column] > threshold
    df_f = df[mask]

    result = {
        "filtered_data": df_f.to_dict(orient="list"),
        "count": df_f.shape[0]
    }

    return result