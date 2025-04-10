import streamlit as st
import pandas as pd
from st_components import st_select_multiple_files

st.title("File Upload Example")

# This function will create a file uploader widget that accepts 
# multiple CSV files and previews them and returns combined dataframe.
df = st_select_multiple_files() 
st.write("Combined CSV files preview")
st.dataframe(df.head()) 
