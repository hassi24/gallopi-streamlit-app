import streamlit as st

st.title("🎯 Practice Arena")
st.write(f"{st.session_state.avatar} Complete one quick mission.")

lesson = st.selectbox(
    "Choose lesson",
    ["Communication Quest", "Teamwork Trail", "Interview Arena"]
)

if lesson == "Communication Quest":
    st.subheader("Mission 1")
    st.write("A classmate interrupts you during a group presentation. What do you do?")
    ans = st.radio(
        "Pick your move",
        [
            "Stop talking and get angry.",
            "Calmly continue, then address it respectfully after the presentation.",
            "Leave the presentation."
        ],
        key="comm_q1"
    )
    if st.button("Check Answer", key="comm_btn"):
        if ans == "Calmly continue, then address it respectfully after the presentation.":
            st.success("Great choice! +15 XP")
            st.balloons()
            st.session_state.xp += 15
            st.session_state.skill_scores["Communication"] += 3
        else:
            st.error("Not the best choice. Try a calm and professional response.")
            st.session_state.hearts = max(0, st.session_state.hearts - 1)

elif lesson == "Teamwork Trail":
    st.subheader("Mission 2")
    st.write("A teammate misses a deadline. What is the best next step?")
    ans = st.radio(
        "Choose",
        [
            "Blame them in front of everyone.",
            "Discuss it privately and reset the task plan together.",
            "Ignore the issue."
        ],
        key="team_q1"
    )
    if st.button("Check Answer", key="team_btn"):
        if ans == "Discuss it privately and reset the task plan together.":
            st.success("Excellent teamwork! +20 XP")
            st.balloons()
            st.session_state.xp += 20
            st.session_state.skill_scores["Teamwork"] += 3
            if "Team Titan" not in st.session_state.badges:
                st.session_state.badges.append("Team Titan")
        else:
            st.error("Try again with a supportive and professional action.")
            st.session_state.hearts = max(0, st.session_state.hearts - 1)

else:
    st.subheader("Mission 3")
    st.write("Interview prompt: Tell me about yourself.")
    answer = st.text_area("Type your answer")
    if st.button("Score My Answer"):
        if len(answer.strip()) > 40:
            st.success("Nice job! You sound more prepared. +20 XP")
            st.balloons()
            st.session_state.xp += 20
            st.session_state.skill_scores["Confidence"] += 4
            if "Interview Champ" not in st.session_state.badges:
                st.session_state.badges.append("Interview Champ")
        else:
            st.warning("Add more detail about your strengths, background, and goals.")

if st.session_state.xp >= 200:
    st.session_state.level = 2