🏥 Medical Insurance Cost Prediction:

📌 Project Overview
This project is a Machine Learning-based web application that predicts medical insurance costs for individuals based on their personal details such as age, gender, BMI, children, smoker status, and region.
The main objective is to provide an accurate cost estimate using historical insurance data and ML algorithms.

🚀 Features
1) Predicts medical insurance charges 💰
2) User-friendly Streamlit Web App
3) Converts prediction result into Indian Rupees (₹)
4) Clean and interactive UI with background image and emojis ✨
5) Easy to deploy and run locally

📂 Dataset
The dataset used is the popular Medical Insurance Dataset (commonly available on Kaggle).
It contains the following columns:
1) age – Age of the person
2) sex – Gender (male/female)
3) bmi – Body Mass Index
4) children – Number of dependents
5) smoker – Whether the person is a smoker or not
6) region – Residential region
7) charges – Medical insurance cost (Target variable)

🛠️ Tech Stack
Python 🐍
Libraries:
1) pandas, numpy – Data Handling
2) scikit-learn – Machine Learning Model
3) matplotlib, seaborn – Visualization
4) pickle – Model Saving
5) streamlit – Web App

⚙️ How It Works
1) User enters their details in the web app form.
2) The trained ML model processes the input.
3) Predicted insurance cost is displayed in Indian Rupees (₹).


Project Structure
medical-insurance-prediction/
│── App.py                        # Streamlit app
│── medical_insurance_model.pkl    # Trained ML model
│── dataset.csv                    # Dataset (if included)
│── requirements.txt               # Dependencies
│── README.md                      # Documentation

📊 Model Training
1) Preprocessing: Encoding categorical columns (sex, smoker, region).
2) Scaling features if required.
3) Trained regression model (Linear Regression / Random Forest).
4) Saved model using pickle as medical_insurance_model.pkl.

📸 Screenshots:
<img width="1617" height="844" alt="Screenshot 2025-09-12 142105" src="https://github.com/user-attachments/assets/9dc43f67-60a3-4643-9582-e8df130af909" />
<img width="1803" height="732" alt="Screenshot 2025-09-12 142125" src="https://github.com/user-attachments/assets/fa1ce6ae-7e3d-421e-ba8c-d5d9d537d08d" />
<img width="1004" height="824" alt="Screenshot 2025-09-12 142142" src="https://github.com/user-attachments/assets/7282cd59-c13e-47c7-af98-21ad964afefb" />



