from openai import OpenAI
import streamlit as st
import tempfile

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

def transcribe_audio(audio_file):

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    ) as tmp:

        tmp.write(audio_file.read())
        tmp_path = tmp.name

    with open(tmp_path, "rb") as audio:

        transcript = client.audio.transcriptions.create(
            model="gpt-4o-mini-transcribe",
            file=audio
        )

    return transcript.text