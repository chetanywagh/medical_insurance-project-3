import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title & Description
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f0f6ff;
    }
    .main {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    }
    .form-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #007BFF, #00C6FF);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px 28px;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0056b3, #0094cc);
        color: white;
    }
  .result-card {
        background: #e9fdf0;
        padding: 18px;
        border-left: 6px solid #28a745;
        border-radius: 10px;
        margin-top: 25px;
        font-size: 20px;
        font-weight: 600;
        color: #155724;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with image + text (side by side)
col1, col2 = st.columns([1,6])  # adjust ratio for alignment
with col1:
    st.image("medical_codt_prediction image.png", width=90)  # apna logo file ka naam yeh rakho
with col2:
    st.markdown(
        "<h1 style='color:#007BFF; font-size: 42px;'>Medical Insurance Prediction</h1>",
        unsafe_allow_html=True
    )

# Description
st.write(
    "This app predicts medical insurance costs based on user details. "
    "Please fill in the form below and click Predict"
)

# User inputs in 2-column layout
st.header("User Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

with col2:
    sex = st.selectbox("Sex", ["male", "female"])
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Data Preprocessing (encoding)
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0
region_dict = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region = region_dict[region]

# Prepare features
features = np.array([[age, bmi, children, sex, smoker, region]])

# USD to INR conversion rate
USD_TO_INR = 83

# Predict button
if st.button("Predict Medical Cost"):
    prediction = model.predict(features)
    cost_usd = prediction[0]
    cost_inr = cost_usd * USD_TO_INR
    st.success(f"💰 Predicted Medical Insurance Cost: ₹{cost_inr:,.2f}")
