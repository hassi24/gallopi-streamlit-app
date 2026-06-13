import streamlit as st

st.title("🎖️ Badges")
st.caption("Unlock badges as you practice and improve.")

cols = st.columns(2)
for i, badge in enumerate(st.session_state.badges):
    with cols[i % 2]:
        if badge["locked"]:
            st.warning(f"Locked: {badge['name']}")
        else:
            st.success(f"Unlocked: {badge['name']}")