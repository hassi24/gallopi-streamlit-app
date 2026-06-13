import streamlit as st
import pandas as pd

st.title("🏆 Leaderboard")

data = pd.DataFrame({
    "Name": ["Aarav", st.session_state.username, "Diya", "Rohan"],
    "XP": [180, st.session_state.xp, 150, 125]
}).sort_values("XP", ascending=False).reset_index(drop=True)

data.index = data.index + 1
st.dataframe(data, use_container_width=True)
st.info("Earn more XP to climb the rank.")