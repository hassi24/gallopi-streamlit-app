import streamlit as st
import pandas as pd

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
    }

if "friends" not in st.session_state:
    st.session_state.friends = []

st.title("🏆 Leaderboard")
st.caption("Compete with your friend circle.")

rows = [
    {
        "name": st.session_state.user.get("name", "You"),
        "xp": st.session_state.user.get("xp", 0),
        "streak": st.session_state.user.get("streak", 0),
        "type": "You",
    }
]

rows += st.session_state.friends

df = pd.DataFrame(rows)
if not df.empty:
    df = df.sort_values(["xp", "streak"], ascending=False).reset_index(drop=True)
    df.index = df.index + 1
    st.dataframe(df, use_container_width=True)

    top = df.iloc[0]
    st.success(f"Current leader: {top['name']} with {top['xp']} XP.")
else:
    st.info("No leaderboard data yet.")
