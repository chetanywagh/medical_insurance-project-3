import streamlit as st
import pickle
import numpy as np
import os

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Logo path
logo_path = os.path.join("images", "medical_codt_prediction image.png")

# Background image
# background_path = "background_image.jpeg"

# Background CSS
st.markdown(
    f"""
    # <style>
    # .stApp {{
    #     background: url("{background_path}");
    #     background-size: cover;
    #     background-position: center;
    #     background-attachment: fixed;
    # }}
    # </style>
    """,
    unsafe_allow_html=True
)

# Show logo
st.image(logo_path, width=90)

# Title and description with emoji
st.title("🏥 Medical Insurance Cost Prediction")
st.markdown(
    "📝 Please fill in the form below and click **Predict** to estimate insurance cost."
)

# Form inputs
age = st.number_input("👤 Age", min_value=1, max_value=100, value=25)
sex = st.selectbox("⚧️ Sex", ["male", "female"])
bmi = st.number_input("📊 BMI", min_value=10.0, max_value=50.0, value=20.0)
children = st.number_input("👶 Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("🚬 Smoker", ["yes", "no"])
region = st.selectbox("🌍 Region", ["southwest", "southeast", "northwest", "northeast"])

# Convert inputs to numeric format for model
sex = 1 if sex == "male" else 0
smoker = 1 if smoker == "yes" else 0
region_map = {"southwest": 0, "southeast": 1, "northwest": 2, "northeast": 3}
region = region_map[region]

features = np.array([[age, sex, bmi, children, smoker, region]])

# Predict button
if st.button("🔮 Predict"):
    prediction = model.predict(features)[0]
    # Dollar → Rupees conversion (approx 1 USD = 83 INR)
    prediction_inr = prediction * 83
    st.success(f"💰 Estimated Insurance Cost: ₹{prediction_inr:,.2f}")
