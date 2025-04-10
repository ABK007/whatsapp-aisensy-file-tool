import streamlit as st
import pandas as pd

st.title("File Upload Example") 


# Create a file uploader widget that accepts CSV files.
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    st.write("Filename:", uploaded_file.name)
    try:
        # Read the CSV file into a DataFrame.
        df = pd.read_csv(uploaded_file)
        st.write("Preview of the CSV file:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error reading file: {e}")