# App.py
import streamlit as st
import pickle
import numpy as np

# -------------------------
# Page config
# -------------------------
st.set_page_config(page_title="Medical Insurance Predictor",
                   page_icon="💙",
                   layout="centered")

# -------------------------
# Model loader with caching
# -------------------------
@st.cache(allow_output_mutation=True)
def load_model(path="medical_insurance_model.pkl"):
    try:
        with open(path, "rb") as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        return None

model = load_model()

# -------------------------
# Custom CSS (professional look)
# -------------------------
st.markdown("""
    <style>
    /* Page background */
    body {
        background-color: #f6f8fa;
    }

    /* Main white card */
    .main-box {
        background: #ffffff;
        padding: 30px 34px;
        border-radius: 14px;
        box-shadow: 0 8px 28px rgba(16, 24, 40, 0.06);
        max-width: 920px;
        margin: 36px auto;
    }

    /* Title */
    .main-box h1 {
        font-size: 34px;
        margin-bottom: 6px;
        color: #111827;
        font-weight: 700;
        text-align: center;
    }
    .main-box .subtitle {
        text-align: center;
        color: #6b7280;
        margin-bottom: 22px;
    }

    /* Button style */
    .stButton>button {
        background-color: #e63922;
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 12px 18px;
        border: none;
        width: 100%;
        font-size: 16px;
        transition: background-color .15s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #c72c18;
    }

    /* Result card */
    .result-card {
        background: #f8fafc;
        border-radius: 10px;
        padding: 16px;
        margin-top: 18px;
        border: 1px solid rgba(15, 23, 42, 0.04);
    }
    .result-title { color: #374151; font-weight: 600; }
    .result-value { font-size: 20px; font-weight: 700; margin-top: 8px; color: #0f172a; }
    .result-note { font-size: 13px; color: #6b7280; margin-top: 6px; }

    /* Make Streamlit labels a bit bolder */
    label {
        font-weight: 600;
        color: #111827;
    }

    /* Slight spacing for form rows */
    .stNumberInput, .stSelectbox {
        margin-bottom: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# App UI inside styled box
# -------------------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.markdown("<h1>Medical Insurance Price Calculator</h1>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter basic details below and click <strong>Check Value</strong> to estimate the cost.</div>', unsafe_allow_html=True)

# Using a form so inputs are submitted together (prevents instant rerun)
with st.form(key="predict_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1, format="%d")
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1, format="%.1f")
        sex = st.selectbox("Sex", ["Male", "Female"])

    with col2:
        children = st.number_input("Children", min_value=0, max_value=10, value=0, step=1, format="%d")
        smoker = st.selectbox("Smoker", ["No", "Yes"])
        region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

    submit = st.form_submit_button("Check Value")

# -------------------------
# Prediction & output
# -------------------------
if submit:
    if model is None:
        st.error("Model not found. Make sure 'medical_insurance_model.pkl' is present in the app directory.")
    else:
        # encode categorical inputs exactly as training
        sex_enc = 1 if sex == "Male" else 0
        smoker_enc = 1 if smoker == "Yes" else 0
        region_map = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
        region_enc = region_map[region]

        # prepare features (shape: 1 x n_features)
        features = np.array([[int(age), float(bmi), int(children), int(sex_enc), int(smoker_enc), int(region_enc)]])

        # predict
        with st.spinner("Predicting..."):
            pred = model.predict(features)
            estimated = float(pred[0])

        # present a professional-looking range (±10%)
        lower = estimated * 0.90
        upper = estimated * 1.10

        # render result card (HTML inside Streamlit markdown)
        st.markdown(f"""
            <div class="result-card">
                <div class="result-title">Estimated insurance range</div>
                <div class="result-value">${lower:,.2f} – ${upper:,.2f}</div>
                <div class="result-note">Point estimate: ${estimated:,.2f}  •  Range shown is ±10% for professional presentation</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
