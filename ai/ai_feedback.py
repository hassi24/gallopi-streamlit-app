import streamlit as st
import google.generativeai as genai
import json

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_answer(question, transcript):

    prompt = f"""
You are Gallopi AI, an expert communication coach.

Question:
{question}

User Answer:
{transcript}

Return ONLY valid JSON in this format:

{{
    "score": 85,
    "clarity": 8,
    "confidence": 8,
    "structure": 7,
    "relevance": 9,
    "strengths": [
        "Strength 1",
        "Strength 2"
    ],
    "improvements": [
        "Improvement 1",
        "Improvement 2"
    ],
    "improved_answer": "A stronger version of the user's answer."
}}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    # Remove markdown fences if Gemini returns them
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)