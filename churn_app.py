import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction App")

age = st.number_input("Age")
gender = st.selectbox("Gender", ["Male","Female"])
tenure = st.number_input("Tenure (months)")
usage = st.number_input("Usage Frequency")
support = st.number_input("Support Calls")
delay = st.number_input("Payment Delay")
stype = st.selectbox("Subscription Type", ["Basic","Standard","Premium"])
contract = st.selectbox("Contract Type", ["Monthly","Quarterly","Annual"])
spend = st.number_input("Total Spend")
last = st.number_input("Last Interaction (Days)")

if st.button("Predict"):
    data = pd.DataFrame({
        "Age":[age],
        "Gender":[gender],
        "Tenure":[tenure],
        "Usage Frequency":[usage],
        "Support Calls":[support],
        "Payment Delay":[delay],
        "Subscription Type":[stype],
        "Contract Length":[contract],
        "Total Spend":[spend],
        "Last Interaction":[last]
    })

    pred = model.predict(data)[0]

    if pred == 1:
        st.error("⚠ Customer will CHURN")
    else:
        st.success("😊 Customer will STAY")
