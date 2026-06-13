import streamlit as st
import pandas as pd

st.title("👤 Profile")
user = st.session_state.user

left, right = st.columns([1, 1.2])
with left:
    st.subheader(user["name"])
    st.write(f"Path: {user['path']}")
    st.write(f"XP: {user['xp']}")
    st.write(f"Streak: {user['streak']}")
    st.write(f"Friends: {user['friends_count']}")
with right:
    st.subheader("Practice history")
    if st.session_state.practice_history:
        df = pd.DataFrame(st.session_state.practice_history)
        st.dataframe(df[["prompt", "score"]], use_container_width=True)
    else:
        st.info("No practice attempts yet.")