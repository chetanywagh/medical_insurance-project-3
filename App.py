import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title & Description
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="centered")

# Custom CSS (sirf button ke liye rakha)
st.markdown(
    """
    <style>
    body {
        background-color: #f0f6ff;
    }
    .stButton>button {
        background-color: #007BFF;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title with image + text
col1, col2 = st.columns([1,6])
with col1:
    st.image("medical_codt_prediction image.png", width=90)
with col2:
    st.markdown(
        "<h1 style='color:#007BFF; font-size: 42px;'>Medical Insurance Prediction</h1>",
        unsafe_allow_html=True
    )

st.write("This app predicts medical insurance costs based on user details. Fill in the form below 👇")

# ================= SIMPLE FORM =================
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

# Predict button
if st.button("Predict Medical Cost"):
    # Encoding
    sex_val = 1 if sex == "male" else 0
    smoker_val = 1 if smoker == "yes" else 0
    region_dict = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
    region_val = region_dict[region]

    # Features
    features = np.array([[age, bmi, children, sex_val, smoker_val, region_val]])

    # Prediction
    USD_TO_INR = 83
    prediction = model.predict(features)
    cost_usd = prediction[0]
    cost_inr = cost_usd * USD_TO_INR
    st.success(f"💰 Predicted Medical Insurance Cost: ₹{cost_inr:,.2f}")
