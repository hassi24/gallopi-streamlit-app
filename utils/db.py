import streamlit as st

def init_state():
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

    if "badges" not in st.session_state:
        st.session_state.badges = [
            {"name": "First Step", "locked": False},
            {"name": "3 Day Spark", "locked": False},
            {"name": "Voice Starter", "locked": True},
            {"name": "Clarity Champ", "locked": True},
            {"name": "Team Player", "locked": True},
        ]

    if "practice_history" not in st.session_state:
        st.session_state.practice_history = []

def seed_data():
    if not st.session_state.friends:
        st.session_state.friends = [
            {"name": "Aisha", "type": "Streak buddy", "xp": 160, "streak": 4},
            {"name": "Rahul", "type": "Mock interview buddy", "xp": 140, "streak": 2},
            {"name": "Sam", "type": "Accountability partner", "xp": 200, "streak": 5},
        ]
        st.session_state.user["friends_count"] = len(st.session_state.friends)

def add_friend(name, friend_type):
    st.session_state.friends.append(
        {"name": name, "type": friend_type, "xp": 100, "streak": 1}
    )
    st.session_state.user["friends_count"] = len(st.session_state.friends)

def complete_assessment(score, band):
    st.session_state.assessment_done = True
    st.session_state.user["assessment_score"] = score
    st.session_state.user["path"] = band
    st.session_state.user["level_name"] = band

def add_xp(points):
    st.session_state.user["xp"] += points

def save_practice(prompt, transcript, feedback, score):
    st.session_state.practice_history.append(
        {
            "prompt": prompt,
            "transcript": transcript,
            "feedback": feedback,
            "score": score,
        }
    )
    add_xp(25)
    unlock_voice_badge()

def unlock_voice_badge():
    for badge in st.session_state.badges:
        if badge["name"] == "Voice Starter":
            badge["locked"] = False