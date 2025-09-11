import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="wide")

# Custom CSS for Hamburger Navbar + Background
st.markdown("""<style>
/* Background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #e0f7fa, #ffffff, #e3f2fd);
    font-family: 'Segoe UI', sans-serif;
}
/* Navbar styling */
.topnav {
    overflow: hidden;
    background: #007BFF;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 100;
    padding: 10px 20px;
    color: white;
}
.hamburger {
    font-size: 26px;
    cursor: pointer;
}
.sidenav {
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 101;
    top: 0;
    left: 0;
    background-color: #111;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}
.sidenav a {
    padding: 12px 24px;
    text-decoration: none;
    font-size: 20px;
    color: #f1f1f1;
    display: block;
    transition: 0.3s;
}
.sidenav a:hover {
    background: #007BFF;
    color: white;
}
.sidenav .closebtn {
    position: absolute;
    top: 15px;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}
</style>

<div class="topnav">
    <span class="hamburger" onclick="openNav()">☰</span> 
    <span style="font-size:20px; margin-left:15px;">Medical Insurance Predictor</span>
</div>

<div id="mySidenav" class="sidenav">
    <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
    <a href="#home">🏠 Home</a>
    <a href="#prediction">📊 Prediction</a>
    <a href="#about">ℹ️ About</a>
</div>

<script>
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
</script>""", unsafe_allow_html=True)

# Home Section
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
st.title("🏠 Welcome to Medical Insurance Predictor")
st.write("""This project helps you **predict medical insurance costs instantly** based on your health
and lifestyle factors.

✅ **What this app does:**  
- Estimates medical insurance premium using ML model  
- Considers Age, BMI, Smoking habits, Region, etc.  
- Gives results in **INR (₹)** for better understanding  

🚀 **Why this project?**  
Medical costs are rising rapidly. This tool helps individuals plan their finances better by 
giving them an **instant estimate** of expected insurance costs.""")  

# Prediction Section
st.markdown("<div id='prediction'></div>", unsafe_allow_html=True)
st.header("📊 Prediction - Enter Your Details")

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

if st.button("💰 Predict Medical Cost"):
    prediction = model.predict(features)
    cost_usd = prediction[0]
    cost_inr = cost_usd * USD_TO_INR
    st.success(f"💰 Predicted Medical Insurance Cost: ₹{cost_inr:,.2f}")

# About Section
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.header("ℹ️ About This Project")
st.write("""This project is developed as part of a **Machine Learning & Data Science portfolio**.  
It demonstrates:  

- 🧠 **ML Model**: Trained on insurance dataset  
- 🎨 **UI**: Built with Streamlit, styled with CSS  
- 💡 **Purpose**: To provide users a tool to predict costs easily  

👨‍💻 **Team Members**:  
- Chetan Wagh  
- Shivani  
- Goutham  
- Manoj  
- Sahil  
- Akhil  

📌 **Mentor**: Mr. B. Harish""")
