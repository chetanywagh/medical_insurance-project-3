import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="wide")

# Background Gradient
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #e0f7fa, #ffffff, #e3f2fd);
        font-family: 'Segoe UI', sans-serif;
    }
    .result-card {
        margin-top: 20px;
        padding: 15px;
        border-radius: 12px;
        background: #f0f8ff;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #333;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
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
    </style>
""", unsafe_allow_html=True)

# ---- Tabs ----
tab1, tab2, tab3 = st.tabs(["🏠 Home", "📊 Prediction", "ℹ️ About Us"])

# ---- Home Tab ----
with tab1:
    st.title("🏠 Welcome to Medical Insurance Predictor")
    st.write("""This project helps you **predict medical insurance costs instantly** based on your health
and lifestyle factors.

 **What this app does:**  
- Estimates medical insurance premium using ML model  
- Considers Age, BMI, Smoking habits, Region, etc.  
- Gives results in **INR (₹)** for better understanding  

 **Why this project?**  
Medical costs are rising rapidly. This tool helps individuals plan their finances better by 
giving them an **instant estimate** of expected insurance costs.""")

# ---- Prediction Tab ----
with tab2:
    st.header(" Prediction - Enter Your Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
        children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)

    with col2:
        sex = st.selectbox("Sex", ["male", "female"])
        smoker = st.selectbox("Smoker", ["yes", "no"])
        region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

    # Preprocessing
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
        # st.success(f" Predicted Medical Insurance Cost: ₹{cost_inr:,.2f}")
        st.markdown(
        f"<div class='result-card'> Predicted Medical Insurance Cost: <br><span style='font-size:26px;'>₹{cost_inr:,.2f}</span></div>",
        unsafe_allow_html=True
    )

# ---- About Tab ----
with tab3:
    st.header(" About This Project")
    st.write("""This project is developed as part of a **Machine Learning & Data Science portfolio**.  
It demonstrates:  

- 🧠 **ML Model**: Trained on insurance dataset  
- 🎨 **UI**: Built with Streamlit, styled with CSS  
- 💡 **Purpose**: To provide users a tool to predict costs easily  

