import streamlit as st
import pandas as pd
import joblib

# Load model, scaler, and columns
model = joblib.load("final_model.pkl")
scaler = joblib.load("scaler.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("Inventory Delay Prediction App")

# Inputs
product_name = st.selectbox("Product Name",[ 
    "S-Cross Zeta","Baleno CVT","Vitara Brezza VXi","S-Cross Alpha",
    "S-Cross Alpha+","S-Cross Delta","Ertiga ZXi","S-Cross Sigma",
    "Ciaz Delta","Ciaz Alpha","Ciaz Zeta","Vitara Brezza LXi",
    "Vitara Brezza AT","Baleno Sigma","Vitara Brezza ZXi+",
    "Ertiga LXi","Swift ZXi+","Swift ZXi","Swift LXi",
    "Ciaz S","Swift AMT","Ciaz Sigma","Ertiga Tour M",
    "Baleno Delta","Vitara Brezza ZXi","Ertiga VXi",
    "Ertiga ZXi+","Swift VXi","Baleno Zeta","Baleno Alpha"
])
model_name = st.selectbox("Model Name", ["S-Cross", "Vitara Brezza", "Ciaz", "Swift", "Baleno", "Ertiga"])
location = st.selectbox("Location", ["Karnataka", "Rajasthan", "Tamilnadu",
             "Maharashtra", "Uttar Pradesh", "West Bengal"])

ordered_qty = st.number_input("Ordered Quantity", 0)
inventory_stock = st.number_input("Inventory Stock", 0)
unit_cost = st.number_input("Unit Cost", 0.0)
order_month = st.number_input("Order Month", 1,12)
order_year = st.number_input("Order Year",2000,2100)
lead_time = st.number_input("Lead Time",0)

if st.button("Predict"):

    # Create dataframe
    input_data = pd.DataFrame({
        "Product Name":[product_name],
        "Model Name":[model_name],
        "Location":[location],
        "Ordered Quantity":[ordered_qty],
        "Inventory Stock Quantity":[inventory_stock],
        "Unit Cost":[unit_cost],
        "Order_Month":[order_month],
        "Order_Year":[order_year],
        "Lead_Time":[lead_time]
    })

    # One-hot encoding (same as training)
    input_data = pd.get_dummies(input_data)

    # Match training columns
    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    # Scaling
    input_data = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Delayed Delivery")
    else:
        st.success("On-Time Delivery")