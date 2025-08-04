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
