import streamlit as st

from ai.ai_feedback import analyze_answer
from ai.speech_to_text import transcribe_audio

from utils.db import save_practice

st.set_page_config(
    page_title="Practice Arena",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ Practice Arena")
st.caption("Practice workplace communication and get AI coaching")

# ==========================================
# CHALLENGE BANK
# ==========================================

CHALLENGES = {

    "🗣 Communication World": {

        "Level 1": [
            "Introduce yourself to a new teammate.",
            "Tell us about one of your strengths.",
            "Describe your communication style."
        ],

        "Level 2": [
            "How would you handle a misunderstanding?",
            "How would you give constructive feedback?",
            "How would you ask for help professionally?"
        ],

        "Level 3": [
            "How would you resolve team conflict?",
            "How would you communicate bad news?",
            "How would you manage expectations?"
        ]
    },

    "💼 Interview World": {

        "Level 1": [
            "Tell me about yourself.",
            "Why do you want this role?",
            "What motivates you?"
        ],

        "Level 2": [
            "Describe a challenge you overcame.",
            "Tell me about a failure.",
            "What are your strengths and weaknesses?"
        ],

        "Level 3": [
            "Describe a leadership experience.",
            "Tell me about a difficult decision.",
            "Describe a conflict you resolved."
        ]
    },

    "🤝 Teamwork World": {

        "Level 1": [
            "Describe a successful team project.",
            "How do you collaborate with others?"
        ],

        "Level 2": [
            "A teammate is not contributing. What do you do?",
            "How would you motivate your team?"
        ],

        "Level 3": [
            "How would you handle conflict between teammates?",
            "How would you lead a struggling project?"
        ]
    },

    "👑 Leadership World": {

        "Level 1": [
            "What makes a good leader?",
            "Describe your leadership style."
        ],

        "Level 2": [
            "How would you motivate an underperforming employee?",
            "How would you delegate work?"
        ],

        "Level 3": [
            "How would you handle a crisis?",
            "Describe a difficult leadership decision."
        ]
    }
}

# ==========================================
# WORLD SELECTION
# ==========================================

world = st.selectbox(
    "🌎 Choose Learning World",
    list(CHALLENGES.keys())
)

level = st.selectbox(
    "📈 Choose Level",
    list(CHALLENGES[world].keys())
)

question = st.selectbox(
    "🎯 Choose Challenge",
    CHALLENGES[world][level]
)

st.markdown("---")

# ==========================================
# RECORD AUDIO
# ==========================================

st.subheader("🎤 Record Your Answer")

audio_value = st.audio_input(
    "Tap to record your response"
)

transcript = ""

if audio_value:

    st.audio(audio_value)

    with st.spinner("Converting speech to text..."):

        try:

            transcript = transcribe_audio(
                audio_value
            )

            st.success(
                "Transcript generated successfully."
            )

        except Exception as e:

            st.error(
                f"Transcription Error: {e}"
            )

# ==========================================
# EDIT TRANSCRIPT
# ==========================================

transcript = st.text_area(
    "📝 Transcript (edit if needed)",
    value=transcript,
    height=220
)

# ==========================================
# ANALYZE
# ==========================================

if st.button(
    "🚀 Analyze With AI",
    use_container_width=True
):

    if not transcript.strip():

        st.warning(
            "Please record your answer first."
        )

        st.stop()

    with st.spinner(
        "Gallopi AI is analyzing..."
    ):

        try:

            result = analyze_answer(
                question,
                transcript
            )

            save_practice(
                question,
                transcript,
                result,
                result["score"]
            )

            st.success(
                f"🏆 Overall Score: {result['score']}/100"
            )

            st.markdown("---")

            c1, c2, c3, c4 = st.columns(4)

            with c1:
                st.metric(
                    "Clarity",
                    result["clarity"]
                )

            with c2:
                st.metric(
                    "Confidence",
                    result["confidence"]
                )

            with c3:
                st.metric(
                    "Structure",
                    result["structure"]
                )

            with c4:
                st.metric(
                    "Relevance",
                    result["relevance"]
                )

            st.markdown("---")

            st.subheader(
                "🌟 Strengths"
            )

            for strength in result["strengths"]:
                st.success(strength)

            st.subheader(
                "📈 Areas To Improve"
            )

            for item in result["improvements"]:
                st.warning(item)

            st.subheader(
                "🎯 AI Coaching Tips"
            )

            if "coaching_tips" in result:

                for tip in result["coaching_tips"]:
                    st.info(tip)

            st.subheader(
                "🤖 Stronger Sample Answer"
            )

            st.info(
                result["improved_answer"]
            )

            st.markdown("---")

            xp_reward = 25

            if level == "Level 2":
                xp_reward = 40

            elif level == "Level 3":
                xp_reward = 60

            st.success(
                f"⚡ XP Earned: {xp_reward}"
            )

            st.balloons()

        except Exception as e:

            st.error(
                f"AI Analysis Error: {e}"
            )

# ==========================================
# PRACTICE HISTORY
# ==========================================

if "practice_history" in st.session_state:

    history = st.session_state.practice_history

    if history:

        st.markdown("---")
        st.subheader("📚 Recent Practice")

        for item in reversed(history[-5:]):

            with st.expander(item["prompt"]):

                st.write(
                    item["transcript"]
                )

                st.write(
                    f"Score: {item['score']}"
                )