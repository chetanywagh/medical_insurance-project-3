import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="centered")

# Custom CSS for Carwale-like design
st.markdown("""
    <style>
    .main-box {
        background: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        max-width: 700px;
        margin: auto;
    }
    h1 {
        text-align: center;
        color: #222;
        font-size: 28px;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #e63922;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px 30px;
        border: none;
        width: 100%;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #c72c18;
    }
    .option-btn {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# UI Layout
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.title("💙 Medical Insurance Price Calculator")

st.markdown("### I am a")
choice = st.radio("", ["Patient", "Doctor"], horizontal=True)

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)

with col2:
    children = st.number_input("Children", min_value=0, max_value=10, value=0)
    smoker = st.selectbox("Smoker", ["Yes", "No"])
    region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

# Encode values
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0
region_dict = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
region = region_dict[region]

# Prepare Features
features = np.array([[age, bmi, children, sex, smoker, region]])

# Prediction Button
if st.button("Check Value"):
    prediction = model.predict(features)
    st.success(f"💰 Predicted Medical Insurance Cost: **${prediction[0]:,.2f}**")

st.markdown('</div>', unsafe_allow_html=True)
