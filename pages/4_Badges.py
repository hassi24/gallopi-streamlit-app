import streamlit as st

st.title("🥇 Badges")

all_badges = [
    "Starter Badge",
    "Team Titan",
    "Interview Champ",
    "Communication Star",
    "Streak Star"
]

for badge in all_badges:
    if badge in st.session_state.badges:
        st.success(f"Unlocked: {badge}")
    else:
        st.warning(f"Locked: {badge}")