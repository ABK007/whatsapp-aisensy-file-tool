import streamlit as st
import pandas as pd

st.title("File Upload Example")


# Create a file uploader widget that accepts CSV files.
uploaded_files = st.file_uploader(
    "Choose a CSV file", type=["csv"], accept_multiple_files=True
)

if uploaded_files:
    st.write(f"Total files uploaded: {len(uploaded_files)}")
    for uploaded_file in uploaded_files:
        st.write(f"Filename: {uploaded_file.name}")
        try:
            # Process each file; assuming it's a CSV file
            df = pd.read_csv(uploaded_file)
            st.write(f"Preview of {uploaded_file.name}:")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading {uploaded_file.name}: {e}")
