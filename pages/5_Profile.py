import streamlit as st
import pandas as pd

st.title("👤 Profile")
st.write(f"Avatar: {st.session_state.avatar}")
st.write(f"Name: {st.session_state.username}")
st.write(f"XP: {st.session_state.xp}")
st.write(f"Level: {st.session_state.level}")
st.write(f"Hearts: {st.session_state.hearts}")
st.write(f"Streak: {st.session_state.streak}")

scores = pd.DataFrame(
    list(st.session_state.skill_scores.items()),
    columns=["Skill", "Score"]
)
st.dataframe(scores, use_container_width=True)