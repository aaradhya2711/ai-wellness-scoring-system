import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("wellness_model.pkl", "rb"))

st.title("AI-Based Wellness Scoring System")

st.write("Enter your health and lifestyle details:")

gender_label = st.selectbox("Gender", ["Male", "Female"])
smoking_label = st.selectbox("Smoking Habit", ["No", "Yes"])
alcohol_label = st.selectbox("Alcohol Consumption", ["No", "Yes"])

# Convert UI input to model input
gender = 0 if gender_label == "Male" else 1
smoking = 1 if smoking_label == "Yes" else 0
alcohol = 1 if alcohol_label == "Yes" else 0
physical = st.slider("Physical Activity Level (1=Low, 3=High)", 1, 3)
fastfood = st.slider("Fast Food Consumption (0=Rare, 3=Daily)", 0, 3)
mental = st.slider("Mental Health Frequency (0=Good, 2=Anxiety)", 0, 2)
sleep = st.slider("Sleep Duration (1=Poor, 4=Excellent)", 1, 4)
sleep_issues = st.selectbox("Sleep Issues", [0, 1])
diet = st.slider("Diet Type (0=Junk, 2=Healthy)", 0, 2)
water = st.slider("Water Intake (0=Low, 2=High)", 0, 2)

if st.button("Predict Wellness Score"):
    input_data = np.array([[gender, smoking, alcohol, physical,
                             fastfood, mental, sleep, sleep_issues,
                             diet, water]])
    
    score = model.predict(input_data)[0]

    st.success(f"Your Wellness Score: {round(score, 2)}")

    if score < 40:
        st.error("Wellness Level: Poor")
    elif score < 60:
        st.warning("Wellness Level: Average")
    elif score < 80:
        st.info("Wellness Level: Good")
    else:
        st.success("Wellness Level: Excellent")
