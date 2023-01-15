#First, you'll need to import the necessary libraries, including streamlit, pandas, pandas-profiling, and re:
import streamlit as st
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
import re

#Next, you'll need to create a function to check the file format of the uploaded file. You can use the re library to check if the file name matches the desired file format (e.g. .csv, .xlsx, .xls). If the file format is not valid, you can use Streamlit's st.warning function to display a warning message to the user and ask them to re-upload the file using the desired file format.

 
#Next, you can use Streamlit's st.file_uploader function to allow the user to upload a file. You can then pass the uploaded file to the check_file_format function to ensure that it's in the desired format. If the file format is valid, you can use the pandas library to read in the file.
uploaded_file = st.file_uploader("Please upload your file", type=["csv", "xlsx", "xls"])
if uploaded_file:
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith("xlsx") or uploaded_file.name.endswith("xls"):
        df = pd.read_excel(uploaded_file)
            
#After reading the file, you can use the pandas_profiling library to generate a data profiling report. You can use the ProfileReport class to create the report, and then display it using Streamlit's st.write function.
    profile = ProfileReport(df)
    st.pyplot(profile.to_widgets())

    #st.write("Data Profiling Report", profile)
    st.write("Dataframe",data)
