import streamlit as st

from ai.speech_to_text import transcribe_audio
from ai.ai_feedback import analyze_answer

from utils.db import save_practice

st.set_page_config(
    page_title="Practice Arena",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ Practice Arena")
st.caption("Level up your communication skills with AI-powered coaching")

# ====================================
# CHALLENGE DATABASE
# ====================================

CHALLENGES = {

    "🗣 Communication World": {

        "Level 1": [
            "Introduce yourself to a new teammate.",
            "Tell us about one of your strengths."
        ],

        "Level 2": [
            "How would you give constructive feedback?",
            "How would you handle a misunderstanding?"
        ],

        "Level 3": [
            "How would you resolve a conflict in a team?",
            "How would you communicate bad news professionally?"
        ]
    },

    "💼 Interview World": {

        "Level 1": [
            "Tell me about yourself.",
            "Why do you want this role?"
        ],

        "Level 2": [
            "Describe a challenge you overcame.",
            "What are your strengths and weaknesses?"
        ],

        "Level 3": [
            "Describe a time you showed leadership.",
            "Tell me about a difficult decision."
        ]
    },

    "🤝 Teamwork World": {

        "Level 1": [
            "How do you work in teams?",
            "Describe a successful collaboration."
        ],

        "Level 2": [
            "A teammate is not contributing. What would you do?",
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
            "How would you handle a major crisis?",
            "Describe a difficult leadership decision."
        ]
    }
}

# ====================================
# WORLD SELECTION
# ====================================

world = st.selectbox(
    "Choose Learning World",
    list(CHALLENGES.keys())
)

level = st.selectbox(
    "Choose Level",
    list(CHALLENGES[world].keys())
)

question = st.selectbox(
    "Choose Challenge",
    CHALLENGES[world][level]
)

st.markdown("---")

# ====================================
# RECORD SECTION
# ====================================

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
                f"Transcription error: {e}"
            )

# ====================================
# TRANSCRIPT
# ====================================

transcript = st.text_area(
    "Transcript (edit if needed)",
    value=transcript,
    height=220
)

# ====================================
# ANALYSIS
# ====================================

if st.button(
    "🚀 Analyze With AI",
    use_container_width=True
):

    if not transcript.strip():

        st.warning(
            "Please record an answer first."
        )

        st.stop()

    with st.spinner(
        "Your AI coach is analyzing..."
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

            c1,c2,c3,c4 = st.columns(4)

            with c1:
                st.metric(
                    "📝 Clarity",
                    f"{result['clarity']}/10"
                )

            with c2:
                st.metric(
                    "💪 Confidence",
                    f"{result['confidence']}/10"
                )

            with c3:
                st.metric(
                    "🏗 Structure",
                    f"{result['structure']}/10"
                )

            with c4:
                st.metric(
                    "🎯 Relevance",
                    f"{result['relevance']}/10"
                )

            st.markdown("---")

            st.subheader(
                "🌟 Strengths"
            )

            for item in result["strengths"]:
                st.success(item)

            st.subheader(
                "📈 Areas to Improve"
            )

            for item in result["improvements"]:
                st.warning(item)

            st.subheader(
                "🤖 Improved Sample Answer"
            )

            st.info(
                result["improved_answer"]
            )

            st.markdown("---")

            st.subheader(
                "🏅 XP Earned"
            )

            xp_reward = 25

            if level == "Level 2":
                xp_reward = 40

            if level == "Level 3":
                xp_reward = 60

            st.success(
                f"You earned {xp_reward} XP!"
            )

            st.balloons()

        except Exception as e:

            st.error(
                f"AI Analysis Error: {e}"
            )