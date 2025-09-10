import streamlit as st
import pickle
import numpy as np
import os

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

# ✅ Load Model with error handling
@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "medical_cost_model.pkl")
    try:
        return pickle.load(open(model_path, "rb"))
    except FileNotFoundError:
        st.error("❌ Model file not found! Please upload `medical_cost_model.pkl` in the same directory as App.py.")
        return None

model = load_model()

# ✅ Main App Layout
st.markdown('<div class="main-box">', unsafe_allow_html=True)
st.title("💊 Medical Insurance Cost Prediction")

# --- Input fields ---
age = st.number_input("Enter Age", min_value=1, max_value=100, step=1)
sex = st.selectbox("Select Gender", ["Male", "Female"])
bmi = st.number_input("Enter BMI", min_value=10.0, max_value=50.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# --- Prediction Button ---
if model is not None and st.button("Predict"):
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
