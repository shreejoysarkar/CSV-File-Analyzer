# CSV-File-Analyzer
A Python script that reads a CSV file and gives quick insights.

---

## 🔍 Problem Statement

Manually inspecting raw CSV files is often tedious and error-prone. This project aims to automate the initial analysis of any CSV file by:
- Displaying structural information (column names and data types)
- Previewing top and bottom records
- Counting unique values per column
- Exporting a cleaned version of the file for further analysis

---

## Click here to check the application : 
https://csv-file-analyzer.streamlit.app/

## 📁 Key Files and Folders

- **`.streamlit/`**  
  Contains configuration file for theme of Streamlit app UI.

- **`sample_datasets/`**  
  Stores built-in CSV files used for demo purposes in the app. These datasets can be loaded without uploading any files, helping users explore features instantly.

- **`analyse.py`**  
  The main Python script that runs the Streamlit application. It handles CSV file uploads, displays basic data insights, and generates visualizations like bar plots, line plots, and pie charts.

- **`trails.ipynb`**  
  A Jupyter notebook used for testing and developing specific features before final deployment. ***This notebook contains all the data analysis and visualization code***

## 🚀 Features

### ✅ Upload Your Own CSV File
Easily upload any `.csv` file and get instant data analysis results.

### ✅ Choose from Sample Datasets
Includes two built-in datasets:
- _Indian Kids Screentime (2025)_
- _Social Media Engagement Metrics_

### 🧹 Data Cleaning
- Automatically drops missing and duplicate rows to ensure clean visualizations.

### 📋 Data Overview
- Dataset shape and column info
- Data types
- Null value summary

### 📊 Descriptive Statistics
- Summary statistics for all columns

### 📌 Value Counts
- Frequency counts for selected columns

### 📈 Visualizations

- **Bar Plot**  
  Visualize the mean of a numerical column grouped by a categorical column.

- **Line Plot**  
  Plot relationships between any two numerical features.

- **Pie Chart**  
  View category distributions with smaller slices grouped into “Others” to avoid clutter.

---
