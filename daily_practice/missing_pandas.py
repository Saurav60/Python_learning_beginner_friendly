import pandas as pd
def handle_missing_values(data):
    df = pd.DataFrame(data)
    for column in df.columns:
        if df[column].isnull().any() and pd.api.types.is_numeric_dtype(df[column]):
            median_value = df[column].median()
            df[column].fillna(value=median_value, inplace=True)
    return df
