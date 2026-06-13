import streamlit as st
import pandas as pd

st.title("🏆 Leaderboard")
st.caption("Compete with your friend circle.")

rows = [{"name": st.session_state.user["name"], "xp": st.session_state.user["xp"], "streak": st.session_state.user["streak"], "type": "You"}]
rows += st.session_state.friends

df = pd.DataFrame(rows).sort_values(["xp", "streak"], ascending=False).reset_index(drop=True)
df.index = df.index + 1
st.dataframe(df, use_container_width=True)

top = df.iloc[0]
st.success(f"Current leader: {top['name']} with {top['xp']} XP.")