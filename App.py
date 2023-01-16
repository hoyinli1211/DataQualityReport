#First, you'll need to import the necessary libraries, including streamlit, pandas, pandas-profiling, and re:
import streamlit as st
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
import re

def introduction():
    st.subheader("Introduction to Data Profiling")
    st.markdown("Data profiling is the process of examining the content, structure, and quality of a dataset. It helps to understand the characteristics of the data, identify patterns and anomalies, and to check for data inconsistencies and errors.")
    st.markdown("There are several key aspects of data profiling, including:")
    st.markdown("1. **Data Structure**: Examining the data structure includes understanding the data types of each column, the number of columns and rows, and the relationships between tables.")
    st.markdown("2. **Data Content**: Examining the data content includes understanding the distribution of values, identifying outliers, and examining the completeness of the data.")
    st.markdown("3. **Data Quality**: Examining the data quality includes identifying missing and duplicate data, identifying data errors, and checking for consistency across columns and tables.")
    st.markdown("4. **Data Validation**: Validation is the process of checking that the data meets certain criteria, such as data types, ranges, and formats.")
    st.markdown("5. **Data Distribution**: Distribution analysis is used to check the frequency of different values in the dataset.")
    st.markdown("6. **Data Correlation**: Correlation analysis is used to check the relationship between different variables in the dataset.")
    st.markdown("Data profiling can be done using various tools, such as pandas_profiling, DataExplorer, and DataWrangler, and also using Python libraries like pandas, numpy, and matplotlib.")
    st.markdown("It's important to understand that data profiling is a crucial step in the data preparation process, as it helps to identify issues that need to be addressed before the data can be used for analysis or modeling.")
    
    st.subheader("pandas_profiling Python package")
    st.markdown("`pandas_profiling` is a powerful Python library that allows you to quickly generate a comprehensive report on your data. It's built on top of the popular data manipulation library `pandas`, and provides a range of useful features, such as:")
    st.markdown("1. **Overview report**: The overview report provides a high-level summary of the data, including information on the number of rows, columns, and missing values. It also includes warnings, such as highly correlated variables and large numbers of duplicate observations.")
    st.markdown("2. **Interactive inspection**: The report allows you to explore the data in more detail, by clicking on the icons next to each variable. This allows you to view the distribution of the data, examine the correlation between variables, and see the top and bottom records for each variable.")
    st.markdown("3. **Variables types**: The report shows the type of each variable, whether it's categorical, numerical, or boolean, and provides statistics such as the mean, median, mode, and standard deviation.")
    st.markdown("4. **Missing values**: The report shows the percentage of missing values in each variable, and allows you to quickly identify which variables have a high percentage of missing data.")
    st.markdown("5. **Customizable**: You can customize the report by passing various parameters, such as setting the maximum number of variables to show in the report, or specifying which variables to exclude.")
    st.markdown("Overall, `pandas_profiling` is a great tool for quickly gaining insights into your data, and is a valuable addition to any data scientist's toolbox.")
    
    st.subheader("How to fill the missing values?")
    st.markdown("When filling missing values in a dataset, it's important to consider the type of data and the distribution of the values.")
    st.markdown("- **Mean**: The mean is the sum of the values divided by the number of values. It's a commonly used measure of central tendency for numerical data. It's a good choice for filling missing values when the data is numerical and is normally distributed. This is because the mean is sensitive to outliers and if the data is not normally distributed, then the mean may not be a good representation of the center of the data.")
    st.markdown("- **Median**: The median is the middle value of a dataset when the values are arranged in order. It's a commonly used measure of central tendency for numerical data and it's less sensitive to outliers than the mean. It's a good choice for filling missing values when the data is numerical and is not normally distributed or if there are outliers.")
    st.markdown("- **Mode**: The mode is the value that occurs most frequently in a dataset. It's commonly used for categorical data, but it can also be used for numerical data, although it's not as common as using mean or median. It's a good choice for filling missing values when the data is categorical or if the data is numerical and is not normally distributed and there are outliers, and if you want to prioritize the most frequent value in the data.")
    st.markdown("It's important to note that these are general guidelines and the best method for filling missing values will depend on the specific dataset and the context of the problem. It is always good to check the distribution of the data, inspect the correlation among the variables, and consider the domain knowledge before making a decision.")
    
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

def load_data(link):
    df = pd.read_csv(link)
    st.session_state['df'] = df
    return df

def showdata(df):
    # Display the imported file in data frame
    df=st.session_state['df']
    st.write("Dataframe",df)
    
    if st.button('Run Data Quality Check'):
        # Generate the data profiling report
        profile = ProfileReport(df)
        # Display the report in the Streamlit app
        st.components.v1.html(profile.to_html(), height=2000, scrolling=True)

with tab_uploadnreport:

# Allow the user to upload a file
    st.subheader("Upload File and Generate Report")
    uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx", "xls"])
    if st.button("Import sample dataset"):
        df = load_data("https://raw.githubusercontent.com/hoyinli1211/DataQualityReport/main/loan_sanction_test.csv")
        showdata(df)
        
    if uploaded_file is not None:
        if uploaded_file.name.endswith("csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith("xlsx") or uploaded_file.name.endswith("xls"):
            df = pd.read_excel(uploaded_file)
        showdata(df)

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
                
