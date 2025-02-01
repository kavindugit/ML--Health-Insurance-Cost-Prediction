import os
os.system('streamlit run app.py')

import streamlit as st
import numpy as np
import pandas as pd
from prediction_helper import predict
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Page configuration
st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide")

# App title
st.title("Health Insurance Cost Predictor")

# Layout with equal-width columns
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    age = st.number_input("Age", min_value=18, step=1, max_value=100)
    genetical_risk = st.number_input("Genetical Risk", min_value=0, step=1, max_value=5)
    gender = st.selectbox("Gender", ["Male", "Female"])
    smoking_status = st.selectbox("Smoking Status", ["No Smoking", "Regular", "Occasional"])

with col2:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, step=1, max_value=20)
    insurance_plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])
    marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])
    region = st.selectbox("Region", ["Northwest", "Southeast", "Southwest", "Northeast"])

with col3:
    income_lakhs = st.number_input("Income in Lakhs", min_value=0, step=1, max_value=200)
    employment_status = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Freelancer", "nan"])
    bmi_category = st.selectbox("BMI Category", ["Normal", "Obesity", "Overweight", "Underweight"])
    medical_history = st.selectbox("Medical History", [
        "Diabetes", "High blood pressure", "No Disease", "Diabetes & High blood pressure", "Thyroid",
        "Heart disease", "High blood pressure & Heart disease", "Diabetes & Thyroid", "Diabetes & Heart disease"
    ])

input_dict = {
    "age": age,
    "gender": gender,
    "marital_status": marital_status,
    "number_of_dependants": number_of_dependants,
    "bmi_category": bmi_category,
    "smoking_status": smoking_status,
    "employment_status": employment_status,
    "income_lakhs": income_lakhs,
    "region": region,
    "medical_history": medical_history,
    "insurance_plan": insurance_plan,
    "genetical_risk": genetical_risk,
}

# Prediction button
if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f"Predicted Insurance Cost: {prediction}")
