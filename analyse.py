

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configure Streamlit page
st.set_page_config(page_title="CSV Quick Insights", layout="wide")
st.title(" CSV Quick Insights App")

# Section: File Upload
st.header(" Upload CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded
if uploaded_file is not None:
    try:
        # Read CSV into DataFrame
        df = pd.read_csv(uploaded_file)

        st.success(" File uploaded successfully!")

        # Section: Raw Data Preview
        st.header(" Raw Data Preview")
        st.dataframe(df.head())

        # Section: Basic Information
        st.header(" Dataset Overview")
        st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
        st.write("**Column Types:**")
        st.write(df.dtypes)

        # Section: Data Cleaning & Preprocessing
        st.header("🧹 Data Cleaning & Preprocessing")

        # Handling missing values
        missing_counts = df.isnull().sum()
        st.subheader(" Missing Values Count")
        st.write(missing_counts[missing_counts > 0] if missing_counts.any() else "No missing values!")

        # Option to drop rows with missing values
        if missing_counts.any():
            if st.checkbox("Drop rows with missing values?"):
                df = df.dropna()
                st.info("Dropped missing values. Updated dataset:")
                st.write(df.head())

        # Convert columns to appropriate types (optional: date)
        if st.checkbox("Try parsing date columns automatically?"):
            for col in df.columns:
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    continue
            st.success("Attempted to parse datetime columns.")

        # Section: Descriptive Statistics
        st.header("Descriptive Statistics")
        st.write(df.describe(include='all'))

        # Section: Correlation Heatmap
        st.header("Correlation Heatmap (Numerical Columns Only)")
        numeric_df = df.select_dtypes(include=['number'])
        if not numeric_df.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(numeric_df.corr(), annot=True, cmap="YlGnBu", ax=ax)
            st.pyplot(fig)
        else:
            st.warning("No numeric columns available for correlation analysis.")

        # Section: Column-wise Visualization
        st.header("Column-wise Visualization")
        selected_col = st.selectbox("Select a column to visualize", df.columns)

        if pd.api.types.is_numeric_dtype(df[selected_col]):
            st.bar_chart(df[selected_col].head(50))
            st.line_chart(df[selected_col].head(50))
        elif pd.api.types.is_object_dtype(df[selected_col]) or pd.api.types.is_categorical_dtype(df[selected_col]):
            top_vals = df[selected_col].value_counts().head(10)
            fig, ax = plt.subplots()
            top_vals.plot(kind='bar', ax=ax)
            ax.set_title(f"Top 10 Value Counts in '{selected_col}'")
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
        elif pd.api.types.is_datetime64_any_dtype(df[selected_col]):
            df[selected_col] = pd.to_datetime(df[selected_col])
            df['Year'] = df[selected_col].dt.year
            st.line_chart(df['Year'].value_counts().sort_index())

    except Exception as e:
        st.error(f"Error reading file: {e}")

else:
    st.info("⬆Please upload a CSV file to begin.")

# Footer
st.markdown("---")
st.markdown("Built using Python, Pandas, Matplotlib, Seaborn, and Streamlit")
