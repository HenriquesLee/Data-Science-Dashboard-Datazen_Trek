# Interactive Data Science Dashboard

Welcome to the **Interactive Data Science Dashboard** – a Streamlit-based interactive platform that allows users to explore datasets, visualize correlations, and train machine learning models (currently featuring linear regression).

This project was developed as part of the **Datazen Trek Project by me,Lee Henriques**.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [File Structure](#file-structure)
- [License](#license)

## Overview

This dashboard is designed for interactive data analysis and machine learning tasks. It allows users to:
- Upload CSV datasets
- Perform data cleaning
- Visualize data with heatmaps, pair plots, and regression plots
- Build and evaluate multiple machine learning models (including linear and multiple regression)

## Features

- **Interactive Data Exploration**: Upload and explore datasets with interactive visualizations, including correlation matrices and pair plots.
  
- **Regression Modeling**: Supports training of multiple linear regression models, allowing users to select feature and target variables, with performance metrics like R², MAE, MSE, and RMSE.
  
- **Data Cleaning**: Automatically cleans the dataset, handling missing values and preparing the data for analysis.
  
- **Responsive UI**: The dashboard is built with a responsive design, ensuring smooth user experience on devices of various screen sizes.
  
- **Custom Visualizations**: Visualize regression lines and residuals to understand model fit, with options to plot residuals for multiple regression features.
  
- **No-Code Interface**: Designed for non-technical users to run advanced data analysis without writing code.

 
## Installation

To run this project locally, follow these steps:

### Prerequisites
Make sure you have Python 3.x installed on your system.

### Clone the Repository
```bash
git clone https://github.com/HenriquesLee/Data-Science-Dashboard-Datazen_Trek.git
```

### Install Dependencies
You can install all required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

The main libraries used include:
- `streamlit` for the dashboard interface
- `pandas` for data handling
- `numpy` for numerical operations
- `seaborn` and `matplotlib` for visualizations
- `scikit-learn` for machine learning models

## How to Use

1. **Start the App**:
   Run the following command to launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. **Upload a Dataset**:
   Upload a CSV file using the file uploader in the sidebar.

3. **Explore Data**:
   - Preview the raw and cleaned data.
   - Select features and target variables for visualizations and model training.

4. **Visualize**:
   - View the correlation matrix and pair plots of the selected features.
   - Plot regression lines and residuals.

5. **Train Model**:
   - Train a linear or multiple regression model.
   - Evaluate the model using metrics like R², MAE, MSE, and RMSE.

## File Structure

```
├── app.py                    # Main Streamlit application
├── utils
│   ├── data_utils.py          # Functions for data loading and cleaning
│   ├── visualization_utils.py # Functions for visualizations
│   ├── model_utils.py         # Functions for training and evaluating models
├── requirements.txt           # List of required Python packages
└── README.md                  # Project documentation
```

### Key Files

- **`app.py`**: This is the main file that contains the Streamlit application.
- **`data_utils.py`**: Contains functions for loading and cleaning data.
- **`visualization_utils.py`**: Functions for generating visualizations like correlation heatmaps, pair plots, and regression lines.
- **`model_utils.py`**: Includes functions to train and evaluate machine learning models (linear regression, etc.).

## License

This project is licensed under the **GNU General Public License**. See the [LICENSE](LICENSE) file for more details.
