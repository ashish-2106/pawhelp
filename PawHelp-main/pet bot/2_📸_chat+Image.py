from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-pro-vision")  
def getGemini_response(input, image):
    if input!= "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content([image])

    return response.text


st.set_page_config(page_title="Google gemini chatbot", page_icon="🐾")
st.title("Personal GPT for inatant assistance of your pet")
st.subheader("Give us the image or tell what is happning to the animal")
st.sidebar.success("How can I help you")


input = st.text_input("Input prompt: " , key="input")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
submit = st.button("Give me the response")

if submit:
    response = getGemini_response(input,image)
    st.subheader("Hey this is SEVA BOT and this is your response")
    st.write(response)