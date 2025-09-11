import streamlit as st
import pickle
import numpy as np

# Load model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="centered")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f9fbfd;
        font-family: "Segoe UI", sans-serif;
    }
    .title {
        font-size: 42px;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #007BFF, #00C6FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #444;
        margin-bottom: 30px;
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

# Title
st.markdown("<h1 class='title'>💙 Medical Insurance Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predict your expected medical insurance costs by filling in the details below 👇</p>", unsafe_allow_html=True)

# Form Card
with st.container():
    st.markdown("<div class='form-card'>", unsafe_allow_html=True)
    st.subheader("📝 User Information")

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

# Predict Button
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

    # Result Card
    st.markdown(
        f"<div class='result-card'>💰 Predicted Medical Insurance Cost: ₹{cost_inr:,.2f}</div>",
        unsafe_allow_html=True
    )
