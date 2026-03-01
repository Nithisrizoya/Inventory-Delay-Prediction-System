# Inventory-Delay-Prediction-System

# Project Overview

This project is a Machine Learning-based Inventory Delay Prediction System built to predict whether a product delivery will be:

- ✅ On-Time Delivery

- ⚠ Delayed Delivery

The model helps businesses reduce delays, improve supply chain efficiency, and make data-driven decisions.

# Problem Statement

In inventory management, delays cause:

- Increased operational cost

- Customer dissatisfaction

- Supply chain disruption

This project aims to build a classification model to predict delivery delays using historical inventory data.

# Dataset Features

**Main Columns Used:**

- Product Name

- Model Name

- Ordered Quantity

- Supplier

- Location

- Inventory Stock Quantity

- Unit Cost

- Order Month

- Order Year

- Lead Time

- Stock Difference

- Lead Time Category

- Inventory Stress

- Peak Month Indicator

- Log Transformed Features

- Aging Score

**Target Variable:**

- Delay Status

0 → On-Time Delivery

1 → Delayed Delivery

# **Technologies Used**

- Python

- Pandas

- NumPy

- Scikit-Learn

- XGBoost

- Matplotlib / Seaborn

- Streamlit (for deployment)

# Workflow

- Data Cleaning

- Exploratory Data Analysis (EDA)

- Feature Engineering

- Feature Selection

- Train-Test Split (Stratified)

- Model Training

- Model Evaluation

- Streamlit Deployment

# Machine Learning Models Used

- Logistic Regression

- Decision Tree

- Random Forest

- K-Nearest Neighbors

- XGBoost

# Best Performing Model:

Random Forest

Accuracy: ~86% (after proper feature engineering)

# Evaluation Metrics

- Accuracy

- Confusion Matrix

- Precision

- Recall

- F1-Score

- Cross Validation

# Business Impact

- Reduces delivery delays

- Improves supplier performance analysis

- Helps in proactive inventory planning

- Supports data-driven decision making

# Future Improvements

- Hyperparameter tuning

- Advanced feature selection

- Deployment on cloud

- Real-time data integration
