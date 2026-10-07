import streamlit as st
import joblib
from preprocessing import clean_text

# ---------- Page settings ----------
st.set_page_config(
    page_title="Review Sentiment",
    page_icon="💬",
    layout="centered",
)


# ---------- Model ----------
@st.cache_resource
def load_model():
    return joblib.load("lr_model.pkl")


model = load_model()

label_map = {0: "negative", 1: "neutral", 2: "positive"}

THEME = {
    "positive": {"emoji": "😊", "color": "#1E8E5A", "bg": "#E8F6EF", "text": "This review sounds happy with the product."},
    "neutral":  {"emoji": "😐", "color": "#B7791F", "bg": "#FFF6E0", "text": "This review is mixed or doesn't take a clear side."},
    "negative": {"emoji": "😞", "color": "#C53030", "bg": "#FDECEC", "text": "This review sounds unhappy with the product."},
}

EXAMPLES = {
    "😊 Positive": "Absolutely love this! Great quality, arrived early, and works exactly as described.",
    "😐 Neutral": "It's okay. Does the job but nothing special, and the packaging was average.",
    "😞 Negative": "Stopped working after two days. Waste of money and customer support never replied.",
}


# ---------- Styling ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'DM Sans', sans-serif;
    }
    .stApp { background: #F1F3F6; }
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 1.5rem; max-width: 760px; }

    /* Header band */
    .hero {
        background: #232F3E;
        border-bottom: 5px solid #FF9900;
        border-radius: 14px;
        padding: 2rem 2rem 1.7rem 2rem;
        margin-bottom: 1.5rem;
    }
    .hero h1 {
        color: #FFFFFF;
        font-size: 2rem;
        font-weight: 700;
        margin: 0 0 .4rem 0;
        padding: 0;
        letter-spacing: -0.02em;
    }
    .hero p { color: #C9D1DB; margin: 0; font-size: 1rem; line-height: 1.5; }

    /* Input card */
    .section-title {
        font-weight: 700;
        color: #232F3E;
        font-size: 1.05rem;
        margin: .2rem 0 .5rem 0;
    }
    .stTextArea textarea {
        border-radius: 10px;
        border: 1.5px solid #CBD3DD;
        background: #FFFFFF;
        font-size: 1rem;
        line-height: 1.5;
        color: #232F3E;
    }
    .stTextArea textarea:focus {
        border-color: #FF9900;
        box-shadow: 0 0 0 3px rgba(255,153,0,.25);
    }
    .stTextArea label { display: none; }

    /* Buttons */
    div.stButton > button {
        border-radius: 999px;
        border: 1.5px solid #CBD3DD;
        background: #FFFFFF;
        color: #232F3E;
        font-weight: 500;
        padding: .35rem 1rem;
        transition: border-color .15s, background .15s;
    }
    div.stButton > button:hover {
        border-color: #FF9900;
        background: #FFF8EB;
        color: #232F3E;
    }
    div.stButton > button[kind="primary"] {
        background: #FF9900;
        border-color: #FF9900;
        color: #131A22;
        font-weight: 700;
        border-radius: 10px;
        padding: .6rem 1rem;
        font-size: 1.05rem;
    }
    div.stButton > button[kind="primary"]:hover {
        background: #F08804;
        border-color: #F08804;
        color: #131A22;
    }

    /* Result */
    .result {
        border-radius: 14px;
        padding: 1.4rem 1.5rem;
        margin-top: 1.2rem;
        display: flex;
        gap: 1rem;
        align-items: center;
    }
    .result .emoji { font-size: 3rem; line-height: 1; }
    .result .label { font-size: 1.7rem; font-weight: 700; line-height: 1.1; }
    .result .note { color: #3B4756; margin-top: .25rem; }

    /* Confidence bars */
    .bars { background: #FFFFFF; border-radius: 14px; padding: 1.1rem 1.4rem; margin-top: .9rem; }
    .bar-row { display: flex; align-items: center; gap: .8rem; margin: .5rem 0; }
    .bar-name { width: 80px; font-weight: 500; color: #232F3E; text-transform: capitalize; }
    .bar-track { flex: 1; height: 10px; background: #E6EAF0; border-radius: 999px; overflow: hidden; }
    .bar-fill { height: 100%; border-radius: 999px; }
    .bar-pct { width: 52px; text-align: right; font-weight: 700; color: #232F3E; }

    .hint { color: #6B7787; font-size: .85rem; margin-top: .3rem; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Header ----------
st.markdown(
    """
    <div class="hero">
        <h1>💬 Review Sentiment</h1>
        <p>Paste a product review and find out if it reads as positive, neutral, or negative.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------- Input ----------
if "review" not in st.session_state:
    st.session_state.review = ""


def set_example(text):
    st.session_state.review = text


st.markdown('<div class="section-title">Your review</div>', unsafe_allow_html=True)

review = st.text_area(
    "Enter your review:",
    key="review",
    height=150,
    placeholder="Example: I really love this product!",
)
st.markdown(
    f'<div class="hint">{len(review)} characters</div>', unsafe_allow_html=True
)

st.markdown('<div class="section-title" style="margin-top:1rem">Try an example</div>', unsafe_allow_html=True)
cols = st.columns(3)
for col, (name, text) in zip(cols, EXAMPLES.items()):
    col.button(name, on_click=set_example, args=(text,), use_container_width=True)

st.write("")
predict = st.button("Analyze sentiment", type="primary", use_container_width=True)


# ---------- Prediction ----------
if predict:
    if review.strip() == "":
        st.warning("Write or paste a review above, then select Analyze sentiment.")
    else:
        with st.spinner("Reading the review..."):
            cleaned_review = clean_text(review)
            prediction = model.predict([cleaned_review])[0]
            sentiment = label_map.get(prediction, prediction)

        t = THEME[sentiment]

        st.markdown(
            f"""
            <div class="result" style="background:{t['bg']}; border-left:6px solid {t['color']};">
                <div class="emoji">{t['emoji']}</div>
                <div>
                    <div class="label" style="color:{t['color']};">{sentiment.capitalize()}</div>
                    <div class="note">{t['text']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Confidence bars (only if the model supports probabilities)
        if hasattr(model, "predict_proba"):
            try:
                probs = model.predict_proba([cleaned_review])[0]
                rows = ""
                for cls, p in sorted(zip(model.classes_, probs), key=lambda x: -x[1]):
                    name = label_map.get(cls, str(cls))
                    color = THEME[name]["color"] if name in THEME else "#888"
                    rows += (
                        f'<div class="bar-row">'
                        f'<div class="bar-name">{name}</div>'
                        f'<div class="bar-track"><div class="bar-fill" '
                        f'style="width:{p*100:.1f}%; background:{color};"></div></div>'
                        f'<div class="bar-pct">{p*100:.0f}%</div>'
                        f"</div>"
                    )
                st.markdown(
                    f'<div class="bars"><div class="section-title">Model confidence</div>{rows}</div>',
                    unsafe_allow_html=True,
                )
            except Exception:
                pass
