import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("ImpactAI – Health Risk Predictor")

age = st.number_input("Age", 1, 100)
bp = st.number_input("Blood Pressure")
sugar = st.number_input("Blood Sugar Level")
bmi = st.number_input("BMI")

if st.button("Predict Risk"):
    input_data = np.array([[age, bp, sugar, bmi]])
    prediction = model.predict(input_data)

    if prediction[0] == 0:
        st.success("Low Health Risk")
    elif prediction[0] == 1:
        st.warning("Medium Health Risk")
    else:
        st.error("High Health Risk – Consult a doctor")
