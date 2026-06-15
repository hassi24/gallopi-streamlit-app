import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

print("AVAILABLE MODELS:\n")

for m in genai.list_models():
    print(m.name)