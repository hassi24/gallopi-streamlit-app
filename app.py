import streamlit as st
from utils.db import init_state, seed_data, add_friend, complete_assessment
from utils.helpers import inject_css, level_from_score, progress_to_next_level

st.set_page_config(
    page_title="Gallopi: Your Soft Skills Journey",
    page_icon="🦙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

init_state()
seed_data()
inject_css()

if "assessment_done" not in st.session_state:
    st.session_state.assessment_done = False

if "show_friend_modal" not in st.session_state:
    st.session_state.show_friend_modal = False

user = st.session_state.user

top_left, top_mid, top_right = st.columns([1.2, 2, 1.2])
with top_left:
    st.markdown("<div class='brand'>🦙 <span>Gallopi</span></div>", unsafe_allow_html=True)
with top_mid:
    xp_pct = progress_to_next_level(user["xp"])
    st.markdown(
        f"""
        <div class="hero-bar">
            <div>
                <div class="muted">Daily goal</div>
                <div class="hero-title">{user["daily_goal"]} XP target</div>
            </div>
            <div class="xp-wrap">
                <div class="xp-pill">🔥 {user["streak"]} day streak</div>
                <div class="xp-pill">⚡ {user["xp"]} XP</div>
                <div class="xp-pill">🏅 {user["level_name"]}</div>
            </div>
        </div>
        <div class="progress-shell">
            <div class="progress-fill" style="width:{xp_pct}%;"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with top_right:
    c1, c2 = st.columns(2)
    with c1:
        if st.button("➕ Add Friend", use_container_width=True):
            st.session_state.show_friend_modal = not st.session_state.show_friend_modal
    with c2:
        st.button("🎯 Daily Quest", use_container_width=True)

if st.session_state.show_friend_modal:
    with st.container(border=True):
        st.subheader("Add a friend")
        friend_name = st.text_input("Friend name", placeholder="Aisha / Rahul / Sam")
        friend_goal = st.selectbox("Friend vibe", ["Streak buddy", "Mock interview buddy", "Accountability partner"])
        if st.button("Save friend"):
            if friend_name.strip():
                add_friend(friend_name.strip(), friend_goal)
                st.success(f"{friend_name} added to your circle.")
                st.session_state.show_friend_modal = False
                st.rerun()

if not st.session_state.assessment_done:
    st.markdown(
        """
        <div class="card hero-card">
            <div class="tag">START HERE</div>
            <h1>Find your current soft-skills level</h1>
            <p>
                Take a quick baseline check so Gallopi can adapt your challenges,
                speaking drills, and feedback style to your current level.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("baseline_assessment"):
        st.subheader("Quick baseline test")
        q1 = st.slider("How confident are you in speaking up during team discussions?", 1, 5, 3)
        q2 = st.slider("How well do you handle conflict or missed deadlines?", 1, 5, 3)
        q3 = st.slider("How clearly can you explain your ideas in a structured way?", 1, 5, 3)
        q4 = st.slider("How comfortable are you in mock interviews or presentations?", 1, 5, 3)
        q5 = st.selectbox(
            "What sounds most like you right now?",
            [
                "I need help expressing myself clearly.",
                "I can speak, but I need more structure and confidence.",
                "I speak fairly well and want polishing, precision, and presence.",
            ],
        )
        submitted = st.form_submit_button("Unlock my path")

    if submitted:
        score = q1 + q2 + q3 + q4
        if q5.startswith("I need help"):
            score += 2
        elif q5.startswith("I can speak"):
            score += 4
        else:
            score += 6

        band = level_from_score(score)
        complete_assessment(score, band)
        st.success(f"You’ve been placed into {band}. Your dashboard and practice path are now personalized.")
        st.rerun()

else:
    left, right = st.columns([1.45, 1])

    with left:
        st.markdown(
            f"""
            <div class="card welcome-card">
                <div class="tag">TODAY'S MISSION</div>
                <h2>Welcome back, {user["name"]} 👋</h2>
                <p>You are currently in the <b>{user["level_name"]}</b> path. Keep your streak alive with one speaking rep today.</p>
                <div class="stats-grid">
                    <div class="stat-box"><span>🔥</span><strong>{user["streak"]}d</strong><label>Streak</label></div>
                    <div class="stat-box"><span>⚡</span><strong>{user["xp"]}</strong><label>XP</label></div>
                    <div class="stat-box"><span>🏆</span><strong>{len(st.session_state.badges)}</strong><label>Badges</label></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Choose your next practice")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown(
                """
                <div class="mini-card">
                    <div class="emoji">🎙️</div>
                    <h4>Speak Up</h4>
                    <p>Record your answer to a real workplace prompt and get analysis.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                """
                <div class="mini-card">
                    <div class="emoji">🧠</div>
                    <h4>Quick Reflex</h4>
                    <p>Short scenario drills for confidence and response agility.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                """
                <div class="mini-card">
                    <div class="emoji">🤝</div>
                    <h4>Friend Challenge</h4>
                    <p>Compete on streaks, XP, and shared practice goals.</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.info("Use the left sidebar pages to open Speaking Practice, Leaderboard, Badges, and Profile.")

    with right:
        st.markdown(
            """
            <div class="card side-card">
                <div class="tag">WHY THIS FEELS BETTER</div>
                <h3>More Duolingo-like interaction</h3>
                <ul>
                    <li>Placement first.</li>
                    <li>Speaking reps over passive MCQs.</li>
                    <li>Immediate constructive feedback.</li>
                    <li>XP, streaks, friend loop, and unlocks.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.session_state.friends:
            st.markdown("### Friend circle")
            for friend in st.session_state.friends[:4]:
                st.markdown(
                    f"""
                    <div class="friend-row">
                        <div>
                            <strong>{friend['name']}</strong>
                            <div class="muted">{friend['type']}</div>
                        </div>
                        <div class="xp-pill">🔥 {friend['streak']}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )