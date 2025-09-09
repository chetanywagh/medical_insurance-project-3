import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title & Description
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="centered")

# Custom CSS
st.markdown("""
    <style>
    body{
        background-color: #f0f6ff;
    }
    .main{
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
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
    h1 {
        color: #007BFF;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title with GIF
col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image("doc.gif", use_container_width=True)
st.title("Medical Insurance Prediction")
st.write("This app predicts **medical insurance costs** based on user details.Please fill in the form below and click **Predict**")

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

# Predict button
if st.button("Predict Medical Cost"):
    prediction = model.predict(features)
    st.success(f"Predicted Medical Insurance Cost: ${prediction[0]:,.2f}")
