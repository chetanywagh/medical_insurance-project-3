import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
    /* Background gradient */
    body {
        background: linear-gradient(135deg, #e0f7fa, #ffffff, #e3f2fd);
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background: rgba(255,255,255,0.85);
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0px 6px 25px rgba(0,0,0,0.15);
        backdrop-filter: blur(6px);
    }
    .stButton>button {
        background: linear-gradient(90deg, #007BFF, #00C6FF);
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 14px 30px;
        font-size: 17px;
        border: none;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #0056b3, #0094cc);
        transform: scale(1.05);
    }
    .form-card {
        background: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    # .result-card {
    #     background: #f0fff4;
    #     padding: 20px;
    #     border-left: 6px solid #28a745;
    #     border-radius: 12px;
    #     margin-top: 25px;
    #     font-size: 22px;
    #     font-weight: 600;
    #     color: #155724;
    #     text-align: center;
    # }
    h1 {
        font-size: 44px !important;
        font-weight: 800 !important;
        color: #007BFF !important;
        margin-bottom: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header with logo and title
col1, col2 = st.columns([1,6])
with col1:
    st.image("medical_codt_prediction image.png", width=90)
with col2:
    st.markdown("<h1>Medical Insurance Prediction</h1>", unsafe_allow_html=True)

# Sub description
st.markdown(
    "<p style='font-size:18px; color:#333;'>💡 Get an instant estimate of your medical insurance cost. <br> "
    "Fill in your details below and see the result instantly 👇</p>",
    unsafe_allow_html=True
)

# Input form
st.markdown("<div class='form-card'>", unsafe_allow_html=True)
st.header(" User Information")
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

with col2:
    sex = st.selectbox("Sex", ["male", "female"])
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

st.markdown("</div>", unsafe_allow_html=True)

# Data Preprocessing
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0
region_dict = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region = region_dict[region]

# Features
features = np.array([[age, bmi, children, sex, smoker, region]])

# Conversion rate
USD_TO_INR = 83

# Predict button
if st.button(" Predict Medical Cost"):
    prediction = model.predict(features)
    cost_usd = prediction[0]
    cost_inr = cost_usd * USD_TO_INR

    st.markdown(
        f"<div class='result-card'> Predicted Medical Insurance Cost: <br><span style='font-size:26px;'>₹{cost_inr:,.2f}</span></div>",
        unsafe_allow_html=True
    )
