# utils/db.py


import streamlit as st

# ==========================
# LEVEL SYSTEM
# ==========================

LEVELS = [
    (0, "Beginner"),
    (100, "Communicator I"),
    (250, "Communicator II"),
    (500, "Professional Speaker"),
    (800, "Workplace Expert"),
    (1200, "Leadership Pro"),
    (1800, "Gallopi Master"),
]

# ==========================
# INIT STATE
# ==========================

def init_state():

    if "user" not in st.session_state:

        st.session_state.user = {

            "name": "Friend",
            "avatar": "🐴",

            "xp": 120,
            "streak": 3,

            "daily_goal": 180,

            "level_name": "Beginner",

            "assessment_score": None,
            "path": "Not set",

            "friends_count": 0,

            "league": "Bronze",

            "completed_challenges": 0,
        }

    if "friends" not in st.session_state:

        st.session_state.friends = []

    if "badges" not in st.session_state:

        st.session_state.badges = [

            {
                "name": "First Step",
                "locked": False
            },

            {
                "name": "3 Day Spark",
                "locked": False
            },

            {
                "name": "Voice Starter",
                "locked": True
            },

            {
                "name": "Clarity Champ",
                "locked": True
            },

            {
                "name": "Interview Champ",
                "locked": True
            },

            {
                "name": "Team Player",
                "locked": True
            },

            {
                "name": "Leadership Star",
                "locked": True
            },

            {
                "name": "XP Master",
                "locked": True
            }
        ]

    if "practice_history" not in st.session_state:

        st.session_state.practice_history = []


# ==========================
# SEED DATA
# ==========================

def seed_data():

    if not st.session_state.friends:

        st.session_state.friends = [

            {
                "name": "Aisha",
                "type": "Streak buddy",
                "xp": 320,
                "streak": 5
            },

            {
                "name": "Rahul",
                "type": "Mock interview buddy",
                "xp": 270,
                "streak": 3
            },

            {
                "name": "Sam",
                "type": "Accountability partner",
                "xp": 540,
                "streak": 8
            }
        ]

        st.session_state.user["friends_count"] = len(
            st.session_state.friends
        )


# ==========================
# FRIENDS
# ==========================

def add_friend(name, friend_type):

    st.session_state.friends.append({

        "name": name,
        "type": friend_type,

        "xp": 100,
        "streak": 1
    })

    st.session_state.user["friends_count"] = len(
        st.session_state.friends
    )


# ==========================
# ASSESSMENT
# ==========================

def complete_assessment(score, band):

    st.session_state.assessment_done = True

    st.session_state.user["assessment_score"] = score

    st.session_state.user["path"] = band

    st.session_state.user["level_name"] = band


# ==========================
# XP SYSTEM
# ==========================

def add_xp(points):

    st.session_state.user["xp"] += points

    update_level()

    update_league()

    unlock_badges()


# ==========================
# LEVEL PROGRESSION
# ==========================

def update_level():

    xp = st.session_state.user["xp"]

    current_level = "Beginner"

    for required_xp, level_name in LEVELS:

        if xp >= required_xp:
            current_level = level_name

    st.session_state.user["level_name"] = current_level


# ==========================
# LEAGUES
# ==========================

def update_league():

    xp = st.session_state.user["xp"]

    if xp >= 1500:
        league = "Diamond"

    elif xp >= 1000:
        league = "Platinum"

    elif xp >= 700:
        league = "Gold"

    elif xp >= 400:
        league = "Silver"

    else:
        league = "Bronze"

    st.session_state.user["league"] = league


# ==========================
# BADGES
# ==========================

def unlock_badges():

    xp = st.session_state.user["xp"]

    completed = st.session_state.user[
        "completed_challenges"
    ]

    for badge in st.session_state.badges:

        if badge["name"] == "Voice Starter":

            if completed >= 1:
                badge["locked"] = False

        elif badge["name"] == "Clarity Champ":

            if completed >= 5:
                badge["locked"] = False

        elif badge["name"] == "Interview Champ":

            if completed >= 10:
                badge["locked"] = False

        elif badge["name"] == "Team Player":

            if completed >= 15:
                badge["locked"] = False

        elif badge["name"] == "Leadership Star":

            if completed >= 20:
                badge["locked"] = False

        elif badge["name"] == "XP Master":

            if xp >= 1000:
                badge["locked"] = False


# ==========================
# SAVE PRACTICE
# ==========================

def save_practice(
    prompt,
    transcript,
    feedback,
    score
):

    st.session_state.practice_history.append({

        "prompt": prompt,

        "transcript": transcript,

        "feedback": feedback,

        "score": score
    })

    st.session_state.user[
        "completed_challenges"
    ] += 1

    # XP based on score

    if score >= 90:

        add_xp(60)

    elif score >= 80:

        add_xp(50)

    elif score >= 70:

        add_xp(40)

    else:

        add_xp(25)

    unlock_badges()


# ==========================
# LEADERBOARD
# ==========================

def get_leaderboard():

    leaderboard = []

    leaderboard.append({

        "name":
        st.session_state.user["name"],

        "xp":
        st.session_state.user["xp"]
    })

    leaderboard.extend(
        st.session_state.friends
    )

    leaderboard.sort(
        key=lambda x: x["xp"],
        reverse=True
    )

    return leaderboard

