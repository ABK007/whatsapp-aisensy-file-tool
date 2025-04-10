import streamlit as st
import pandas as pd

def st_select_multiple_files():
    """ Create a file uploader widget that accepts multiple CSV files and preview them. 
    Also returns the combined dataframe of all uploaded files."""
    uploaded_files = st.file_uploader(
        "Choose a CSV file", type=["csv"], accept_multiple_files=True
    )
    
    df_list = []  # List to hold dataframes for each uploaded file
    combined_df = pd.DataFrame()  # Initialize an empty dataframe for combined data

    if uploaded_files:
        st.write(f"Total files uploaded: {len(uploaded_files)}")
        for uploaded_file in uploaded_files:            
            try:
                # Process each file; assuming it's a CSV file
                df = pd.read_csv(uploaded_file)
                st.write(f"#### Uploaded file preview: {uploaded_file.name}")
                st.dataframe(df.head())
                
                # add and combine the dataframes to the list
                df_list.append(df)
                
                combined_df = pd.concat(df_list, ignore_index=True)
                
            except Exception as e:
                st.error(f"following error occurred: {e}")
                
        return combined_df
    
    else:
        return None  # Return None if no files are uploaded
                
