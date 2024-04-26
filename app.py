import os
import streamlit as st
import requests
from PIL import Image
import io

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

def main():
    st.title("Face Composite System")

    ethnicity_race = st.selectbox("Ethnicity/Race", ["Caucasian", "African", "Asian", "Hispanic/Latino", "Middle Eastern", "Indigenous/Aboriginal", "Mixed race"])
    age = st.select_slider("Age", options=[8,16,24,32,40,48,56,64])
    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary/genderqueer"])
    facial_hair = st.selectbox("Facial Hair", ["Beard", "Mustache", "Sideburns", "Clean-shaven"])
    skin_tone = st.selectbox("Skin Tone", ["Fair", "Olive", "Tan", "Dark"])
    scars_marks = st.selectbox("Scars/Marks", ["Birthmarks", "Moles", "Acne scars", "Injury scars"])
    hair_texture = st.selectbox("Hair Texture", ["Straight", "Wavy", "Curly", "Kinky/coiled"])

    if st.button("Generate Composite"):
        text = f"generate  real human face with {{'Ethnicity/Race': '{ethnicity_race}', 'Age': {age}, 'Gender': '{gender}', 'Facial Hair': '{facial_hair}', 'Skin Tone': '{skin_tone}', 'Scars/Marks': '{scars_marks}', 'Hair Texture': '{hair_texture}'}}  "
        image_bytes = query({"inputs": text})
        print(text)
        # Display the image
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption='Generated Composite', use_column_width=True)

if __name__ == "__main__":
    main()
