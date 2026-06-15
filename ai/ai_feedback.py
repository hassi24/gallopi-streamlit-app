from openai import OpenAI
import streamlit as st
import json

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def analyze_answer(prompt, transcript):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"system",
                "content":"""
                You are an expert communication coach.

                Return JSON only.

                Evaluate:

                clarity
                confidence
                structure
                relevance

                Score each out of 10.

                Also return:
                strengths
                improvements
                improved_answer

                Return valid JSON.
                """
            },
            {
                "role":"user",
                "content":f"""
                Question:
                {prompt}

                Answer:
                {transcript}
                """
            }
        ],
        response_format={"type":"json_object"}
    )

    return json.loads(
        response.choices[0].message.content
    )