import streamlit as st
import requests
from PIL import Image
def predict_avc():
 st.title("AVC Prediction")

uploaded_file = st.file_uploader("Upload MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    files = {"file": uploaded_file}
    try:
        response = requests.post("http://localhost:8888/predict", files=files)
        if response.status_code == 200:
            predictions = response.json().get("predictions")
            rec = predictions
            prob_attaint = rec * 100      
            prob_sain = (1-rec) * 100
            image = Image.open(uploaded_file)
            st.image(image)
            if st.button("Voir Résultat"):
                if prob_attaint > 50:
                    st.write("Atteint")
                else:
                    st.write("Sain")
        else:
            st.write("Error:", response.json().get("error"))
    except requests.exceptions.RequestException as e:
        st.write("Error:", e)
