
import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title='Phishing URL Detector', layout='centered')

st.title("🔐 Phishing Website Detector")
st.markdown("Enter basic features to check if a website is **phishing** or **legitimate**.")

# Input features
url_length = st.slider("URL Length", 10, 100, 50)
has_https = st.selectbox("Has HTTPS", [0, 1])
has_ip = st.selectbox("Contains IP Address", [0, 1])
num_dots = st.slider("Number of Dots", 1, 5, 2)
prefix_suffix = st.selectbox("Uses Prefix-Suffix (-)", [0, 1])

if st.button("Predict"):
    model = joblib.load("models/phishing_model.pkl")
    input_data = np.array([[url_length, has_https, has_ip, num_dots, prefix_suffix]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Phishing Website Detected!")
    else:
        st.success("✅ Legitimate Website")
