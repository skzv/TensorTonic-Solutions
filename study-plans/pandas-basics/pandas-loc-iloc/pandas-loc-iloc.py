import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """

    df = pd.DataFrame(data)

    el = df.iloc[row,col]
    d_row = df.iloc[row].values
    d_col = df.iloc[:, col].values
    
    result = [el, d_row, d_col]

    return result