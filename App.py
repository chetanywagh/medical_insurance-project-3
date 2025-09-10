import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("medical_insurance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(page_title="Medical Insurance Predictor", page_icon="💙", layout="centered")

# Custom CSS for Professional Carwale-like Design
st.markdown("""
    <style>
    .main-box {
        background: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        max-width: 700px;
        margin: auto;
    }
    h1 {
        text-align: center;
        color: #1a1a1a;
        font-size: 28px;
        margin-bottom: 25px;
        font-weight: 600;
    }
    .stButton>button {
        background-color: #e63922;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 12px 30px;
        border: none;
        width: 100%;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #c72c18;
    }
    </style>
""", unsafe_allow_html=True)

# UI Box
st.markdown('<div class="main-box">', unsafe_allow_html=Tru
