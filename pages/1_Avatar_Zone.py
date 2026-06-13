from textblob import TextBlob
import streamlit as st

def inject_css():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(180deg,#f7fbff 0%,#eef7f2 100%);
        }
        .brand {
            font-size: 28px;
            font-weight: 800;
            display: flex;
            gap: 10px;
            align-items: center;
            margin-top: 8px;
        }
        .hero-bar, .card, .mini-card, .friend-row {
            background: rgba(255,255,255,0.82);
            border: 1px solid rgba(20,20,20,0.06);
            border-radius: 22px;
            box-shadow: 0 10px 30px rgba(60,90,120,0.08);
        }
        .hero-bar {
            padding: 16px 20px;
            display:flex;
            justify-content:space-between;
            align-items:center;
            gap: 16px;
        }
        .hero-title { font-size: 22px; font-weight: 800; }
        .muted { color:#6b7280; font-size: 13px; }
        .xp-wrap { display:flex; gap:10px; flex-wrap:wrap; justify-content:flex-end; }
        .xp-pill {
            background:#ffffff;
            border-radius:999px;
            padding:8px 12px;
            font-weight:700;
            border:1px solid rgba(0,0,0,0.06);
        }
        .progress-shell {
            width:100%;
            height:14px;
            border-radius:999px;
            background:#dff2ea;
            overflow:hidden;
            margin-top:12px;
        }
        .progress-fill {
            height:100%;
            background:linear-gradient(90deg,#5ee1b2,#7bd3ff);
            border-radius:999px;
        }
        .card {
            padding: 24px;
            margin: 12px 0;
        }
        .hero-card {
            background: linear-gradient(135deg,#baf3df 0%,#cde8ff 70%,#fff1a8 100%);
        }
        .welcome-card {
            background: linear-gradient(135deg,#c8f5e7 0%,#d7ebff 100%);
        }
        .side-card {
            background: linear-gradient(180deg,#ffffff 0%,#f8fffb 100%);
        }
        .tag {
            display:inline-block;
            padding:6px 10px;
            border-radius:999px;
            background:rgba(255,255,255,0.72);
            font-size:12px;
            font-weight:800;
            margin-bottom:10px;
        }
        .stats-grid {
            display:grid;
            grid-template-columns: repeat(3,1fr);
            gap:14px;
            margin-top:18px;
        }
        .stat-box, .mini-card {
            background:#fff;
            border-radius:20px;
            padding:18px;
            border:1px solid rgba(0,0,0,0.05);
        }
        .stat-box span { font-size:26px; display:block; }
        .stat-box strong { font-size:28px; display:block; margin-top:6px; }
        .stat-box label { color:#6b7280; font-size:13px; }
        .mini-card { min-height: 170px; }
        .mini-card .emoji { font-size:28px; margin-bottom:8px; }
        .friend-row {
            padding:14px 16px;
            margin-bottom:10px;
            display:flex;
            justify-content:space-between;
            align-items:center;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def level_from_score(score):
    if score <= 11:
        return "Beginner"
    if score <= 18:
        return "Intermediate"
    return "Advanced"

def progress_to_next_level(xp):
    return min(100, (xp % 200) / 2)

def analyze_speaking_text(text):
    cleaned = text.strip()
    words = cleaned.split()
    word_count = len(words)
    sentence_count = max(1, cleaned.count(".") + cleaned.count("!") + cleaned.count("?"))
    avg_words = word_count / sentence_count

    polarity = TextBlob(cleaned).sentiment.polarity

    clarity = min(10, max(4, round(avg_words / 2)))
    confidence = 8 if polarity >= 0 else 6
    structure = 8 if any(k in cleaned.lower() for k in ["first", "because", "so", "therefore", "next"]) else 6
    relevance = 8 if word_count > 20 else 6

    strengths = []
    improvements = []

    if word_count > 25:
        strengths.append("You gave a reasonably developed answer instead of a one-line response.")
    else:
        improvements.append("Try extending your answer with one example and one clear action step.")

    if structure >= 8:
        strengths.append("Your response shows signs of structure and logical flow.")
    else:
        improvements.append("Use a simple structure like situation → action → result.")

    if confidence >= 8:
        strengths.append("Your tone appears positive and solution-oriented.")
    else:
        improvements.append("Use calmer, more confident phrasing such as 'I would handle this by...'.")

    if not strengths:
        strengths.append("You attempted the prompt, which is the first step toward confidence building.")
    if not improvements:
        improvements.append("Now focus on sharper examples and stronger closing statements.")

    improved_answer = (
        "I would first understand the issue, then speak calmly with the teammate, "
        "clarify the impact on the deadline, and agree on the next step. "
        "If needed, I would update the team early and offer support so the work stays on track."
    )

    score = round((clarity + confidence + structure + relevance) * 2.5)

    return {
        "clarity": clarity,
        "confidence": confidence,
        "structure": structure,
        "relevance": relevance,
        "strengths": strengths,
        "improvements": improvements,
        "improved_answer": improved_answer,
        "score": score,
    }