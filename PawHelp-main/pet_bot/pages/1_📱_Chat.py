from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-pro")  
def getGemini_response(question):
    response = model.generate_content(question) 
    return response.text



# STREAMLIT APPLICATION

st.set_page_config(page_title="Google gemini chatbot", page_icon="🐾")
st.title("Personal GPT for inatant assistance of your pet")
st.sidebar.success("How can I help you")
input=st.text_input("Input: " , key="input")
submit = st.button("Get Response")


if submit:
    response = getGemini_response(input)
    st.subheader("Response to your question is ")
    st.write(response)