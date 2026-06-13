import streamlit as st

st.set_page_config(page_title="Gallopi", page_icon="🐴", layout="wide")

if "username" not in st.session_state:
    st.session_state.username = "Friend"
if "xp" not in st.session_state:
    st.session_state.xp = 120
if "streak" not in st.session_state:
    st.session_state.streak = 3
if "level" not in st.session_state:
    st.session_state.level = 1
if "hearts" not in st.session_state:
    st.session_state.hearts = 3
if "avatar" not in st.session_state:
    st.session_state.avatar = "🐴"
if "badges" not in st.session_state:
    st.session_state.badges = ["Starter Badge"]
if "skill_scores" not in st.session_state:
    st.session_state.skill_scores = {
        "Communication": 72,
        "Teamwork": 68,
        "Confidence": 65,
        "Professionalism": 74
    }

st.markdown("""
<style>
.block-container {padding-top: 1.5rem; padding-bottom: 2rem; max-width: 1100px;}
.main-title {font-size: 3rem; font-weight: 800; color: #1f2937; margin-bottom: 0;}
.sub-title {font-size: 1.2rem; color: #4b5563; margin-top: 0;}
.hero-card {
    background: linear-gradient(135deg, #8BE9C1, #A7D8FF, #FFE08A);
    border-radius: 28px; padding: 28px; color: #123; margin: 16px 0 24px 0;
}
.stat-card {
    background: white; border-radius: 22px; padding: 18px; text-align: center;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06); border: 2px solid #eef2f7;
}
.path-card {
    background: #ffffff; border: 3px solid #d9f99d; border-radius: 22px;
    padding: 18px; margin-bottom: 14px; box-shadow: 0 8px 18px rgba(0,0,0,0.05);
}
.mini-label {font-size: 0.9rem; color: #6b7280;}
.big-score {font-size: 2rem; font-weight: 800; color: #1f2937;}
.avatar-pill {
    display:inline-block; background:#fef3c7; border-radius:999px; padding:8px 14px;
    font-weight:700; margin-bottom:12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='avatar-pill'>{st.session_state.avatar} Gallopi Guide</div>", unsafe_allow_html=True)
st.markdown("<div class='main-title'>Gallopi</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Level up your soft skills, one mission at a time.</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='hero-card'>
    <h2 style='margin:0;'>Welcome back, {st.session_state.username}! {st.session_state.avatar}</h2>
    <p style='font-size:1.1rem; margin-top:10px;'>Your next mission is ready. Keep your streak alive and unlock new confidence powers.</p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"<div class='stat-card'><div class='mini-label'>Hearts</div><div class='big-score'>❤️ {st.session_state.hearts}</div></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='stat-card'><div class='mini-label'>Streak</div><div class='big-score'>🔥 {st.session_state.streak}</div></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='stat-card'><div class='mini-label'>XP</div><div class='big-score'>{st.session_state.xp}</div></div>", unsafe_allow_html=True)
with c4:
    st.markdown(f"<div class='stat-card'><div class='mini-label'>Level</div><div class='big-score'>Lv {st.session_state.level}</div></div>", unsafe_allow_html=True)

st.markdown("## Your journey path")
st.progress(min(st.session_state.xp / 200, 1.0))
st.caption(f"{st.session_state.xp} / 200 XP to next level")

st.markdown("<div class='path-card'><h3>🗣️ Communication Quest</h3><p>Practice professional replies and active listening.</p></div>", unsafe_allow_html=True)
st.markdown("<div class='path-card'><h3>🤝 Teamwork Trail</h3><p>Handle conflict, deadlines, and collaboration challenges.</p></div>", unsafe_allow_html=True)
st.markdown("<div class='path-card'><h3>💼 Interview Arena</h3><p>Train confidence with short recruiter-style questions.</p></div>", unsafe_allow_html=True)

st.page_link("pages/1_Avatar_Zone.py", label="Choose Avatar", icon="🎭")
st.page_link("pages/2_Practice_Arena.py", label="Start Lesson", icon="🎯")
st.page_link("pages/3_Leaderboard.py", label="Leaderboard", icon="🏆")
st.page_link("pages/4_Badges.py", label="Badges", icon="🥇")
st.page_link("pages/5_Profile.py", label="Profile", icon="👤")