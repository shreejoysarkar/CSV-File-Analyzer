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
st.subheader("Example Datasets: ")
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
