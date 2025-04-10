import streamlit as st
import pandas as pd
from st_components import st_select_multiple_files
from functions import add_plus_to_phone

st.title("Creating CSV file for WhatsApp Business API")

# This function will create a file uploader widget that accepts 
# multiple CSV files and previews them and returns combined dataframe.
df = st_select_multiple_files() 

st.markdown("---") # Add a separator line

if df is not None:
    st.write(f"Total rows in combined CSV: {df.shape[0]}")
    st.write(f"Total columns in combined CSV: {df.shape[1]}")
    st.write("### Combined CSV files preview")
    df = add_plus_to_phone(df, column_name="phoneUnformatted") # converting the phone column to start with '+'
    st.dataframe(df.head())

    st.write("### Output CSV Column Selection")


    # Let users select which columns to include in the output CSV.
    selected_columns = st.multiselect(
        "Select columns to include:",
        options=df.columns.tolist(),
        default=df.columns.tolist()
    )

    # For each selected column, allow the user to input a desired output name.
    st.write("### Column Mapping")
    mapping = {}
    for col in selected_columns:
        new_name = st.text_input(f"Output column name for '{col}'", value=col)
        mapping[col] = new_name

    # Show a preview of the DataFrame with renamed columns.
    if selected_columns:
        # Rename only the selected columns, leave the others unchanged if they are not selected.
        df_subset = df[selected_columns].rename(columns=mapping)
        st.write("### Preview of Mapped DataFrame")
        st.dataframe(df_subset)

        # Button to generate CSV
        if st.button("Generate CSV"):
            csv_data = df_subset.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name="mapped_output.csv",
                mime="text/csv"
            )
    else:
        st.warning("Select at least one column to include in the output.")


