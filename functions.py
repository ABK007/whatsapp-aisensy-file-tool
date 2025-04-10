
def add_plus_to_phone(df, column_name="phoneUnformatted"):
    """
    Convert the specified phone column in the DataFrame so that each phone number is a string 
    that starts with a '+'.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the phone column to convert (default "phone_unformatted").
        
    Returns:
        pd.DataFrame: The DataFrame with the modified phone column.
        
    Raises:
        KeyError: If the specified column is not found in the DataFrame.
    """
    if column_name in df.columns:
        # Convert the column to string and ensure each phone number starts with '+'
        df[column_name] = df[column_name].astype(str).apply(lambda x: x if x.startswith('+') else '+' + x)
    else:
        raise KeyError(f"Column '{column_name}' not found in the DataFrame.")
    return df


def remove_blank_rows(df, column_name="phoneUnformatted"):
    """
    Remove the rows in dataframe with empty values or empty strings
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the phone column to convert (default "phone_unformatted").
        
    Returns:
        dataframe with removed empty values rom the specified column.
        
    """
    df_clean = df.dropna(subset=[column_name])    # Remove NaN values first
    df_clean = df_clean[df_clean[column_name] != ''] # Remove empty strings next
    
    return df_clean
