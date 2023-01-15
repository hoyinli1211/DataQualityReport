#First, you'll need to import the necessary libraries, including streamlit, pandas, pandas-profiling, and re:
import streamlit as st
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
import re

def introduction():
    st.subheader("Introduction to Data Profiling")
    st.markdown("Data quality checking is the process of verifying the completeness, accuracy, consistency, and relevance of data. It is an important step in data preparation and data analysis to ensure that the data is suitable for its intended use.")
    st.markdown("There are several ways to perform data inspection using Python, including:")
    st.markdown("- **Manual inspection**: Viewing the data in a spreadsheet or text editor")
    st.markdown("- **Programmatic inspection**: Using Python libraries such as Pandas, NumPy, and Matplotlib to view and analyze the data")
    st.markdown("- **Data profiling**: Using libraries such as pandas_profiling, to generate a report that provides an overview of the data including missing values, data types, and statistics.")

# Create a sidebar on the left side of the app
st.sidebar.title("Instructions")

# Show instructions on how to use the app
st.sidebar.markdown("Step 1: Upload File")
st.sidebar.markdown("- Click on the 'Upload File' button to select a file from your computer.")
st.sidebar.markdown("- Make sure the file is in .csv, .xlsx, .xls format.")
st.sidebar.markdown("Step 2: Run the Report")
st.sidebar.markdown("- Click on the 'Run' button to run the data quality check.")
st.sidebar.markdown("- After running the data quality check, the report will be generated.")
st.sidebar.markdown("- The report will show the data profile, missing values, and correlation.")
st.sidebar.markdown("Step 3: Clean the Data")
st.sidebar.markdown("- Use mean imputation for numeric data (double/float)")
st.sidebar.markdown("- Use median imputation for numeric data (integer)")
st.sidebar.markdown("- Use mode imputation for categorical data")

# Define the main part of the app
st.title("Data Profiling Report")
tabs = st.tabs(["Note","Upload & Generate Report", "Cleansing Recommendation & Export"])

tab_note = tabs[0]

with tab_note:
    introduction()
    
tab_uploadnreport = tabs[1]

with tab_uploadnreport:

# Allow the user to upload a file
    st.subheader("Upload File and Generate Report")
    uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx", "xls"])

    if uploaded_file is not None:
        if uploaded_file.name.endswith("csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith("xlsx") or uploaded_file.name.endswith("xls"):
            df = pd.read_excel(uploaded_file)

        # Display the imported file in data frame
        st.write("Dataframe",df)

        if st.button('Run Data Quality Check'):
        # Generate the data profiling report
            profile = ProfileReport(df)
        # Display the report in the Streamlit app
            st.components.v1.html(profile.to_html(), height=2000, scrolling=True)

tab_cleansingnexport = tabs[2]

with tab_cleansingnexport:
    st.subheader("Data Cleansing Recommendation")
    missing_value_cleansing = st.checkbox("Fill in missing values?")

    # Fill in missing values based on user input
    if missing_value_cleansing and uploaded_file is not None:
        df_clean = df
        for col in df_clean.columns:
            if df_clean[col].dtype == 'float':
                mean = df_clean[col].mean()
                df_clean[col].fillna(mean, inplace=True)
            elif df_clean[col].dtype == 'int':
                median = df_clean[col].median()
                df_clean[col].fillna(median, inplace=True)
            elif df_clean[col].dtype == 'object':
                mode = df_clean[col].mode()[0]
                df_clean[col].fillna(mode, inplace=True)

        st.write("Cleaned data", df_clean)
        st.download_button("Download cleaned data",df_clean.to_csv(index=False), "cleaned_data.csv")
        
        if st.button('Run Data Quality Check on the cleaned data'):
        # Generate the data profiling report
            profile_clean = ProfileReport(df_clean)
        # Display the report in the Streamlit app
            st.components.v1.html(profile_clean.to_html(), width=1000, height=2000, scrolling=True)
                
