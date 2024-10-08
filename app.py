import streamlit as st
import pandas as pd
import numpy as np
from utils.data_utils import load_data, clean_data
from utils.visualization_utils import plot_correlation, plot_pairplot, plot_regression_line, plot_residuals
from utils.model_utils import train_linear_regression, evaluate_model

# Set the background image using HTML and CSS
background_image = """
<style>
[data-testid="stSidebarContent"] {
    background-image: linear-gradient(to bottom right, #290e47, #341c5c);
}
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnJ1bm52Z3FoYXF6bHphZHM3NHMzMzV0a2l6bHd4Z2lsaTNnc3NtZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/TxVVB6PfWMjE4/giphy.gif");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
</style>
"""
st.markdown(background_image, unsafe_allow_html=True)

# Set the app title and description
st.title("Interactive Data Science Dashboard (Lee Henriques - Datazen Trek Project)")
st.subheader("A tool for interactive data analysis and machine learning.")

# Sidebar for data upload
uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV only)", type=["csv"])

# If a file is uploaded
if uploaded_file:
    # Load and preview the data
    df = load_data(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Data Cleaning
    df_clean = clean_data(df)
    st.write("### Cleaned Data")
    st.dataframe(df_clean.head())

    # Feature Selection for Visualization and Regression
    st.write("## Data Visualization and Regression")

    # Allow users to select target and feature columns
    target_col = st.selectbox("Select Target Variable", df_clean.columns)
    feature_cols = st.multiselect("Select Feature Variables", df_clean.columns.drop(target_col))

    if len(feature_cols) > 0:
        # Handle categorical and numeric data
        X = df_clean[feature_cols]
        y = df_clean[target_col]

        # One-Hot Encode categorical features for X
        X = pd.get_dummies(X, drop_first=True)

        # Ensure the target variable is numeric for regression
        if y.dtype == 'object':
            st.warning("Target variable must be numeric. Please select a numeric target column.")
        else:
            # Visualizations
            st.write("## Correlation Matrix")
            plot_correlation(df_clean)

            st.write("## Pair Plot")
            plot_pairplot(df_clean[feature_cols + [target_col]])

            # Train the Linear Regression Model
            st.write("## Linear Regression Model")
            model, predictions = train_linear_regression(X, y)
            st.write("### Model Coefficients", model.coef_)

            # Predictions and Evaluation
            st.write("### Predictions (First 5 Rows)")
            st.write(predictions[:5])

            # Model Evaluation
            r2, mae, mse, rmse = evaluate_model(model, X, y)
            st.write(f"R²: {r2}, MAE: {mae}, MSE: {mse}, RMSE: {rmse}")

            # Plot the regression line for a single feature
            if len(feature_cols) == 1:
                st.write("## Regression Line (Single Feature)")
                plot_regression_line(X.iloc[:, 0], y, predictions)
            elif len(feature_cols) > 1:
                # Residual Plot for Multiple Linear Regression
                st.write("## Residual Plot (Multiple Features)")
                plot_residuals(y, predictions)
else:
    st.write("Upload a CSV file to get started!")
