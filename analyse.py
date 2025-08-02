import streamlit as st
import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.datasets import load_diabetes


# Configure Streamlit page
st.set_page_config(page_title="CSV Quick Insights", layout="wide")
st.title(" CSV Quick Insights App")

# Section: File Upload
st.header(" Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

@st.cache_data
def electronic_details_load():
    return pd.read_csv('sample_datasets\electronic_product_detials.csv')

@st.cache_data
def kid_screentime_load():
    return pd.read_csv('sample_datasets\indian-kids-screentime-2025.csv')

def media_engagements_load():
    return pd.read_csv('sample_datasets\social_media_engagements.csv')


# Initialize session state to track selected dataset and checkboxes
if 'selected_dataset' not in st.session_state:
    st.session_state.selected_dataset = None
    st.session_state.data = None

if 'electronic_detail' not in st.session_state:
    st.session_state.electronic_detail = False

if 'kid_screentime' not in st.session_state:
    st.session_state.kid_screentime = False

if 'media_engagements' not in st.session_state:
    st.session_state.media_engagement = False

def reset_other_checkboxes(selected):
    st.session_state.electronic_detail_checkbox = selected == 'eletronic'
    st.session_state.kid_screentime_checkbox = selected == 'screentime'
    st.session_state.media_engagement_checkbox = selected == 'engagement'

st.markdown('')
st.markdown('')
st.subheader("Sample Datasets: ")
# Streamlit layout with three columns
cole1, cole2, cole3 = st.columns(3)

#loading electronic product details dataset
with cole1:
    if st.checkbox("Use electronic-product-details Dataset", key='electronic_detail', on_change=reset_other_checkboxes, args=('electronic',)):
        if st.session_state.elecctronic_detail_checkbox:
            st.session_state.selected_dataset = 'electronic'
            st.session_state.data = electronic_details_load()
            st.session_state.data.to_csv('sample_datasets\social_media_engagements.csv', index=False)
            data='sample_datasets\social_media_engagements.csv'

# loading indian kids screentime dataset
with cole2:
    if st.checkbox("Use kid-screentime Dataset", key='kid_screentime_checkbox', on_change=reset_other_checkboxes, args=('screentime',)):
        if st.session_state.kid_screentime_checkbox:
            st.session_state.selected_dataset = 'screentime'
            st.session_state.data = kid_screentime_load()
            st.session_state.data.to_csv('sample_datasets/indian-kid-screentime.csv', index=False)
            data='sample_datasets/indian-kid-screentime.csv'

# loading social media engagements dataset
with cole3:
    if st.checkbox("Use social media engagement Dataset", key='media_engagement_checkbox', on_change=reset_other_checkboxes, args=('engagement',)):
        if st.session_state.media_engagement_checkbox:
            st.session_state.selected_dataset = 'engagement'
            st.session_state.data = media_engagements_load()
            st.session_state.data.to_csv('sample_datasets/social_media_engagement.csv', index=False)
            data='sample_datasets/social_media_engagement.csv'

col1, col2, = st.columns(2)

if data is not None:
    df = pd.read_csv(data)
    df.dropna(how='any', inplace=True)
    df.drop_duplicates(keep='first', inplace=True)


    with col2:
        if st.checkbox('Show Full Dataset'):
            st.write(df)
        else:
            st.write(df.head())

    with col1:
        st.subheader("Data Information")
        st.markdown('---')
        st.write('Data Shape:', df.shape)
        st.write('Data Columns:', df.columns)
        st.write('Data Types:', df.dtypes)
        st.write('Data Missing Values:', df.isnull().sum())
        st.markdown('---')

        

    with col2:
        col2.subheader("Descriptive statistics")
        st.write(df.describe(include='all'))
        st.markdown('---')
    
    
    with col2:
        col2.subheader("Value Counts")
        all_columns = df.columns.to_list()
        selected_columns = st.multiselect("Select a selected_columns_names for value counts", all_columns)
        # Check if any columns are selected
        if selected_columns:
            for column_name in selected_columns:
                st.write(df[column_name].value_counts())
        else:
            st.write("Please select at least one column.")
        st.markdown('---')
    
    with col2:
        col2.subheader("Coorelation Plot")
        st.success("")
        # Apply LabelEncoder to string columns
        df_encoded = df.copy()
        le = LabelEncoder()
        for col in df.select_dtypes(include=['object']).columns:
            df_encoded[col] = le.fit_transform(df_encoded[col])
        # Plot correlation matrix using seaborn
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df_encoded.corr(), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
        st.pyplot(fig)
        st.markdown('---')
        
    with col2:
        col2.subheader("Pie Plot")
        st.success("NOTE: Converting the grouping smaller slices into others to aviod cluttering.")
        all_columns = df.columns.to_list()
        column_to_plot = st.selectbox("Select 1 Column for Pie Plot", all_columns)

        # Custom autopct function to format percentage text
        def custom_autopct(pct):
            return ('%.1f%%' % pct) if pct > 0 else ''
        
        fig, ax = plt.subplots(figsize=(8, 6))  # Create a new figure with specified size
        pie_data = df[column_to_plot].value_counts()

        # Threshold for grouping smaller slices into "Others"
        threshold = 0.05  # You can adjust this value as needed
        other_threshold = pie_data.sum() * threshold

        # Create a new Series for the pie chart
        pie_data_adjusted = pie_data.copy()
        pie_data_adjusted['Others'] = pie_data[pie_data < other_threshold].sum()
        pie_data_adjusted = pie_data_adjusted[pie_data_adjusted >= other_threshold]

        # Generate colors for the pie chart
        colors = plt.cm.Paired(range(len(pie_data_adjusted)))

        pie_data_adjusted.plot.pie(
            autopct=custom_autopct, 
            textprops={'fontsize': 10},  # Adjust fontsize for better readability
            ax=ax,
            colors=colors,  # Apply colors
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'},  # Enhance wedge appearance
            startangle=90  # Start the first wedge at 90 degrees
        )
        
        ax.set_ylabel('')  # Remove the default ylabel
        ax.set_title(f'Pie Chart of {column_to_plot}', fontsize=14)  # Set a title
        
        st.pyplot(fig)  # Display the figure in Streamlit

else:
    st.warning("No dataset loaded. Please upload a file or select a dataset.")