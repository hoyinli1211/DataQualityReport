#First, you'll need to import the necessary libraries, including streamlit, pandas, pandas-profiling, and re:
import streamlit as st
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
import re



# Create a sidebar on the left side of the app
st.sidebar.title("Instructions")

# Create a selectbox that allows users to switch between tabs
tabs = ["Upload File", "Generate Report"]
selected_tab = st.sidebar.selectbox("Select a tab", tabs)

# Show instructions for the selected tab
if selected_tab == "Upload File":
    st.sidebar.markdown("- Click on the 'Upload File' button to select a file from your computer.")
    st.sidebar.markdown("- Make sure the file is in .csv, .xlsx, .xls format.")
    st.sidebar.markdown("- Click on the 'Run' button to run the data quality check.")

if selected_tab == "Generate Report":
    st.sidebar.markdown("- After running the data quality check, the report will be generated.")
    st.sidebar.markdown("- The report will show the data profile, missing values, and correlation.")

# Define the main part of the app
st.title("Data Quality Report")

# Allow the user to upload a file
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith("xlsx") or uploaded_file.name.endswith("xls"):
        df = pd.read_excel(uploaded_file)

    # Generate the data profiling report
    profile = ProfileReport(df)

    # Display the report in the Streamlit app
    st.write("Dataframe",df)
    st.components.v1.html(profile.to_html(), height=2000, scrolling=True)
