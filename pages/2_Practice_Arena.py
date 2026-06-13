import streamlit as st
from utils.db import save_practice
from utils.helpers import analyze_speaking_text

st.title("🎙️ Practice Arena")
st.caption("Speak your answer, then get instant constructive feedback.")

prompt = st.selectbox(
    "Choose a workplace challenge",
    [
        "A teammate misses a deadline. What would you say and do?",
        "You disagree with your manager in a meeting. How would you respond respectfully?",
        "Introduce yourself in a mock interview and explain one strength.",
        "A customer is upset. How would you calm the situation?",
    ],
)

st.markdown("### Record your response")
audio_value = st.audio_input("Tap to record your answer")

typed_fallback = st.text_area(
    "Or paste/type your answer here for now",
    placeholder="If transcription is not connected yet, type the answer here to test the feedback engine.",
    height=160,
)

if audio_value:
    st.audio(audio_value)
    st.info("Audio captured successfully. For this version, use the typed response box for analysis or connect your transcription backend next.")

if st.button("Analyze my answer", use_container_width=True):
    if not typed_fallback.strip():
        st.warning("Please record and also paste/type the transcript for analysis in this version.")
    else:
        result = analyze_speaking_text(typed_fallback)
        save_practice(prompt, typed_fallback, result, result["score"])

        a, b, c, d = st.columns(4)
        a.metric("Clarity", f"{result['clarity']}/10")
        b.metric("Confidence", f"{result['confidence']}/10")
        c.metric("Structure", f"{result['structure']}/10")
        d.metric("Relevance", f"{result['relevance']}/10")

        st.success(f"Practice complete. You earned 25 XP. Overall speaking score: {result['score']}/100")

        st.markdown("### What you did well")
        for item in result["strengths"]:
            st.markdown(f"- {item}")

        st.markdown("### What to improve")
        for item in result["improvements"]:
            st.markdown(f"- {item}")

        st.markdown("### Stronger sample answer")
        st.info(result["improved_answer"])