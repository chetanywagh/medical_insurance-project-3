import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="centered")

# Sidebar (Hamburger menu)
menu = st.sidebar.radio("☰ Navigation", ["🏠 Home", "📊 Prediction", "ℹ️ About"])

# Home
if menu == "🏠 Home":
    st.title("Medical Insurance Prediction")
    st.markdown(
        "<p style='font-size:18px; color:#333;'>💡 Welcome to the Medical Insurance Predictor App. <br>"
        "Use this app to get an instant estimate of your medical insurance cost. 👇</p>",
        unsafe_allow_html=True
    )

# Prediction
elif menu == "📊 Prediction":
    st.header(" User Information :")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
        children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

    with col2:
        sex = st.selectbox("Sex", ["male", "female"])
        smoker = st.selectbox("Smoker", ["yes", "no"])
        region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

    # Data Preprocessing
    sex = 1 if sex == "male" else 0
    smoker = 1 if smoker == "yes" else 0
    region_dict = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
    region = region_dict[region]

    features = np.array([[age, bmi, children, sex, smoker, region]])
    USD_TO_INR = 83

    if st.button(" Predict Medical Cost"):
        prediction = model.predict(features)
        cost_usd = prediction[0]
        cost_inr = cost_usd * USD_TO_INR

        st.success(f"💰 Predicted Medical Insurance Cost: ₹{cost_inr:,.2f}")

# About
elif menu == "ℹ️ About":
    st.subheader("About This App")
    st.markdown(
        """
        This **Medical Insurance Predictor** helps you estimate your insurance cost
        based on personal details like age, BMI, smoking habits, and region.  

        🛠️ **Tech Stack**: Python, Streamlit, Machine Learning  
        💡 **Goal**: Provide quick and simple cost estimation for users.  
        """
    )
