import streamlit as st

st.title("🎭 Avatar Zone")
st.write("Pick your learning avatar.")

avatars = ["🐴", "🦄", "🦊", "🐼", "🦁", "🐯"]
cols = st.columns(3)

for i, avatar in enumerate(avatars):
    with cols[i % 3]:
        if st.button(f"{avatar} Select", use_container_width=True):
            st.session_state.avatar = avatar
            st.success(f"Avatar changed to {avatar}")