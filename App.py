import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ✅ Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f9;
        font-family: 'Arial', sans-serif;
    }
    .main-box {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin: 20px auto;
        max-width: 700px;
    }
    h1, h2, h3 {
        color: #2C3E50;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Load model with cache_resource
@st.cache_resource
def load_model():
    return pickle.load(open("medical_cost_model.pkl", "rb"))

model = load_model()

# ✅ Example if you load dataset
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")  # agar data chahiye to use karo

# ✅ Main App Layout
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("💊 Medical Insurance Cost Prediction")

age = st.number_input("Enter Age", min_value=1, max_value=100, step=1)
sex = st.selectbox("Select Gender", ["Male", "Female"])
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

if st.button("Predict"):
    # Encode categorical values
    sex_val = 1 if sex == "Male" else 0
    smoker_val = 1 if smoker == "Yes" else 0
    region_map = {"southwest": 0, "southeast": 1, "northwest": 2, "northeast": 3}
    region_val = region_map[region]

    # Create input array
    input_data = np.array([[age, sex_val, bmi, children, smoker_val, region_val]])

    # Prediction
    prediction = model.predict(input_data)
    st.success(f"✅ Estimated Insurance Cost: ${prediction[0]:.2f}")

st.markdown('</div>', unsafe_allow_html=True)
