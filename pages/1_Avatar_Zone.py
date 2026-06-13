import streamlit as st

if "user" not in st.session_state:
    st.session_state.user = {
        "name": "Friend",
        "xp": 120,
        "streak": 3,
        "daily_goal": 180,
        "level_name": "Level 1",
        "assessment_score": None,
        "path": "Not set",
        "friends_count": 0,
        "avatar_mood": "Friendly Gallopi",
        "theme_energy": "Mint Sky",
    }

if "avatar_mood" not in st.session_state:
    st.session_state.avatar_mood = st.session_state.user.get("avatar_mood", "Friendly Gallopi")

if "theme_energy" not in st.session_state:
    st.session_state.theme_energy = st.session_state.user.get("theme_energy", "Mint Sky")

st.title("🦙 Avatar Zone")
st.caption("Personalize your Gallopi journey.")

col1, col2 = st.columns([1, 1.2])

with col1:
    avatar = st.selectbox(
        "Choose your mascot mood",
        ["Focused Gallopi", "Confident Gallopi", "Friendly Gallopi"],
        key="avatar_mood",
    )

    color = st.selectbox(
        "Theme energy",
        ["Mint Sky", "Sunrise Pop", "Calm Blue"],
        key="theme_energy",
    )

    if st.button("Save avatar style", use_container_width=True):
        st.session_state.user["avatar_mood"] = st.session_state.avatar_mood
        st.session_state.user["theme_energy"] = st.session_state.theme_energy
        st.success("Avatar preferences saved.")

with col2:
    st.markdown("### Your vibe")
    st.markdown(f"- Mascot mood: **{st.session_state.avatar_mood}**")
    st.markdown(f"- Theme energy: **{st.session_state.theme_energy}**")

    if st.session_state.avatar_mood == "Focused Gallopi":
        st.info("You’re choosing a sharp, serious growth vibe.")
    elif st.session_state.avatar_mood == "Confident Gallopi":
        st.info("You’re choosing a bold, interview-ready vibe.")
    else:
        st.info("You’re choosing a warm, playful learning vibe.")

    if st.session_state.theme_energy == "Mint Sky":
        st.success("Fresh and calm UI energy.")
    elif st.session_state.theme_energy == "Sunrise Pop":
        st.warning("Brighter and more energetic UI energy.")
    else:
        st.info("Cool and composed UI energy.")