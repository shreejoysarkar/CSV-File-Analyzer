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
st.title("CSV File Analyzer")


@st.cache_data
def kid_screentime_load():
    return pd.read_csv('sample_datasets/indian-kids-screentime-2025.csv')

@st.cache_data
def media_engagements_load():
    return pd.read_csv('sample_datasets/social_media_engagements.csv')


# ---------- Session State Init ----------
if 'selected_dataset' not in st.session_state:
    st.session_state.selected_dataset = None

if 'data' not in st.session_state:
    st.session_state.data = None

if 'kid_screentime_checkbox' not in st.session_state:
    st.session_state.kid_screentime_checkbox = False

if 'media_engagement_checkbox' not in st.session_state:
    st.session_state.media_engagement_checkbox = False

def reset_other_checkboxes(selected):
    # Reset checkboxes when another is selected
    st.session_state.kid_screentime_checkbox = (selected == 'screentime')
    st.session_state.media_engagement_checkbox = (selected == 'engagement')


# ---------- Upload Section ----------
st.header("Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    st.session_state.data = pd.read_csv(uploaded_file)
    st.session_state.selected_dataset = 'uploaded'
    # Reset sample dataset checkboxes
    st.session_state.kid_screentime_checkbox = False
    st.session_state.media_engagement_checkbox = False

# ---------- Sample Dataset Options ----------
st.subheader("Sample Datasets:")
cole1, cole2, cole3 = st.columns(3)

with cole1:
    if st.checkbox("Use kid-screentime Dataset", key='kid_screentime_checkbox', on_change=reset_other_checkboxes, args=('screentime',)):
        st.session_state.selected_dataset = 'screentime'
        st.session_state.data = kid_screentime_load()

with cole3:
    if st.checkbox("Use social media engagement Dataset", key='media_engagement_checkbox', on_change=reset_other_checkboxes, args=('engagement',)):
        st.session_state.selected_dataset = 'engagement'
        st.session_state.data = media_engagements_load()


# ---------- Display Insights ----------
st.markdown("<hr style='border: 1px solid #ccc;'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

if st.session_state.data is not None:
    df = st.session_state.data.copy()
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
        st.write('Missing Values:', df.isnull().sum())
        st.markdown('---')

    with col2:
        col2.subheader("Descriptive Statistics")
        st.write(df.describe(include='all'))
        st.markdown('---')

    with col2:
        col2.subheader("Value Counts")
        all_columns = df.columns.to_list()
        selected_columns = st.multiselect("Select columns for value counts", all_columns)
        if selected_columns:
            for col in selected_columns:
                st.write(df[col].value_counts())
        else:
            st.write("Please select at least one column.")
        st.markdown('---')

    with col2:
        col2.subheader("Bar Plot")
        st.success("Useful for visualizing categorical vs numerical relationships.")

        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
        numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if categorical_columns and numerical_columns:
            bar_x = st.selectbox("Select Categorical Column (X-axis)", categorical_columns, key='bar_x')
            bar_y = st.selectbox("Select Numerical Column (Y-axis)", numerical_columns, key='bar_y')

            if bar_x and bar_y:
                bar_data = df.groupby(bar_x)[bar_y].mean().sort_values(ascending=False).reset_index()
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.barplot(data=bar_data, x=bar_x, y=bar_y, ax=ax, palette="viridis")
                ax.set_title(f"Bar Plot: Average {bar_y} by {bar_x}")
                ax.set_xlabel(bar_x)
                ax.set_ylabel(f"Average {bar_y}")
                plt.xticks(rotation=45)
                st.pyplot(fig)
        else:
            st.warning("Need at least one categorical and one numerical column.")
        st.markdown('---')

    with col2:
        col2.subheader("Line Plot")
        st.success("Only numerical columns can be plotted.")

        if numerical_columns:
            x_axis = st.selectbox("Select X-axis", numerical_columns, key='line_x')
            y_axis = st.selectbox("Select Y-axis", numerical_columns, key='line_y')

            if x_axis and y_axis:
                fig, ax = plt.subplots(figsize=(10, 5))
                sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
                ax.set_title(f"Line Plot: {y_axis} vs {x_axis}")
                ax.set_xlabel(x_axis)
                ax.set_ylabel(y_axis)
                st.pyplot(fig)
        else:
            st.warning("No numerical columns to plot.")
        st.markdown('---')

    with col2:
        col2.subheader("Pie Plot")
        st.success("Smaller slices grouped as 'Others' to avoid clutter.")
        column_to_plot = st.selectbox("Select 1 Column for Pie Plot", all_columns)

        def custom_autopct(pct):
            return ('%.1f%%' % pct) if pct > 0 else ''

        fig, ax = plt.subplots(figsize=(8, 6))
        pie_data = df[column_to_plot].value_counts()
        threshold = 0.05 * pie_data.sum()
        pie_data_adjusted = pie_data.copy()
        pie_data_adjusted['Others'] = pie_data[pie_data < threshold].sum()
        pie_data_adjusted = pie_data_adjusted[pie_data_adjusted >= threshold]
        colors = plt.cm.Paired(range(len(pie_data_adjusted)))

        pie_data_adjusted.plot.pie(
            autopct=custom_autopct, 
            textprops={'fontsize': 10}, 
            ax=ax,
            colors=colors,
            wedgeprops={'linewidth': 1, 'edgecolor': 'white'},
            startangle=90
        )

        ax.set_ylabel('')
        ax.set_title(f'Pie Chart of {column_to_plot}', fontsize=14)
        st.pyplot(fig)

else:
    st.warning("No dataset loaded. Please upload a file or select a sample dataset.")
