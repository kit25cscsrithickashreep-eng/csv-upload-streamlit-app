import streamlit as st
import pandas as pd

# Title
st.title("CSV File Upload App")

# File uploader
file = st.file_uploader("Upload your CSV file", type=["csv"])

# Check if file is uploaded
if file is not None:
    try:
        # Read CSV file
        df = pd.read_csv(file)

        # Show success message
        st.success("File uploaded successfully!")

        # Display data
        st.subheader("Data Preview")
        st.write(df)

        # Show basic info
        st.subheader("Data Info")
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

    except Exception as e:
        st.error("Error reading file")
        st.write(e)

else:
    st.warning("Please upload a CSV file to continue")