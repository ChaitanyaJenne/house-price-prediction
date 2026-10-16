


import base64
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

MODEL_PATH = Path(__file__).with_name("house_price_model_final_compressed.pkl")
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


model = load_model()


def local_image_background():
    from pathlib import Path
    import base64

    folder = Path(__file__).parent

    for filename in ["house_background.jpg", "house_background.png"]:
        image_path = folder / filename

        if image_path.exists():
            encoded = base64.b64encode(
                image_path.read_bytes()
            ).decode("utf-8")

            mime = "image/png" if filename.endswith(".png") else "image/jpeg"

            return (
                "background-image: linear-gradient("
                "120deg, rgba(9,25,75,.35), rgba(45,30,105,.08)), "
                f"url('data:{mime};base64,{encoded}');"
            )

    return ""


background_css = local_image_background()

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {{
        background:
            radial-gradient(ellipse at 10% 5%, #dbeafe 0%, transparent 36%),
            radial-gradient(ellipse at 95% 20%, #fce7f3 0%, transparent 35%),
            linear-gradient(135deg, #eaf2ff 0%, #f4edff 48%, #e1f8f1 100%);
        font-family: 'Inter', sans-serif;
    }}

    .block-container {{
        max-width: 1450px;
        padding-top: 1.8rem;
        padding-bottom: 2rem;
    }}

    [data-testid="stHeader"] {{
        background: transparent;
    }}

    .hero {{
        {background_css}
        background-size: cover;
        background-position: center;
        background-color: #152b69;
        padding: 2rem 2.2rem;
        border-radius: 24px;
        color: white;
        margin-bottom: 1.3rem;
        box-shadow: 0 14px 35px rgba(34, 52, 120, .20);
        border: 1px solid rgba(255,255,255,.3);
    }}

    .hero h1 {{
        font-size: clamp(2rem, 4vw, 3.6rem);
        font-weight: 800;
        letter-spacing: -1.5px;
        color: white;
        margin: 0;
    }}

    .gradient-word {{
        background: linear-gradient(90deg, #67e8f9, #a5b4fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .hero p {{
        color: #e5edff;
        font-size: 1.05rem;
        margin-top: .5rem;
    }}

    .hero-badges {{
        display: flex;
        gap: .7rem;
        flex-wrap: wrap;
        margin-top: 1.3rem;
    }}

    .hero-badge {{
        background: rgba(255,255,255,.12);
        border: 1px solid rgba(255,255,255,.24);
        padding: .7rem 1rem;
        border-radius: 13px;
        color: white;
        font-size: .88rem;
        backdrop-filter: blur(12px);
    }}

    div[data-testid="stForm"] {{
        background: rgba(255,255,255,.88);
        border: 1px solid rgba(255,255,255,.85);
        border-radius: 22px;
        padding: 1.25rem;
        box-shadow: 0 12px 35px rgba(55,65,120,.12);
    }}

    h2, h3 {{
        color: #14244c;
    }}

    label, [data-testid="stWidgetLabel"] p {{
        color: #18264a !important;
        font-weight: 650 !important;
    }}

    div[data-baseweb="input"] {{
        border-radius: 10px;
    }}

    div[data-testid="stNumberInput"] input {{
        background: #f8faff;
        color: #172554;
        border-radius: 10px;
    }}

    div.stButton > button,
    div[data-testid="stFormSubmitButton"] button {{
        background: linear-gradient(100deg, #078bff, #5145ff 65%, #8b35f5);
        color: white !important;
        border: none;
        border-radius: 12px;
        min-height: 3.2rem;
        font-weight: 750;
        box-shadow: 0 7px 17px rgba(75,75,245,.24);
        transition: transform .15s ease, box-shadow .15s ease;
    }}

    div[data-testid="stFormSubmitButton"] button {{
        width: 100%;
        font-size: 1.05rem;
    }}

    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] button:hover {{
        color: white !important;
        border: none;
        transform: translateY(-2px);
        box-shadow: 0 11px 24px rgba(75,75,245,.32);
    }}

    .result-card {{
        background: linear-gradient(135deg, #ffffff, #e1fff0);
        border: 1px solid #c8f3df;
        border-radius: 22px;
        padding: 1.6rem;
        box-shadow: 0 12px 35px rgba(16,100,75,.12);
        min-height: 220px;
        margin-bottom: 1rem;
    }}

    .result-title {{
        color: #17335d;
        font-size: 1.1rem;
        font-weight: 750;
    }}

    .result-price {{
        color: #08784d;
        font-size: clamp(2rem, 3.5vw, 3.2rem);
        font-weight: 800;
        letter-spacing: -1px;
        margin: .8rem 0 .3rem;
        overflow-wrap: anywhere;
    }}

    .result-sub {{
        display: inline-block;
        color: #08784d;
        background: #d8f8e9;
        border-radius: 999px;
        padding: .4rem .8rem;
        font-weight: 650;
        font-size: .9rem;
    }}

    .notice {{
        background: rgba(16,185,129,.10);
        color: #17664b;
        padding: .9rem;
        margin-top: 1.2rem;
        border-radius: 13px;
        font-size: .86rem;
        line-height: 1.5;
    }}

    .feature-card {{
        background: rgba(255,255,255,.82);
        border: 1px solid rgba(255,255,255,.95);
        border-radius: 20px;
        padding: 1.25rem;
        box-shadow: 0 10px 28px rgba(55,65,120,.10);
    }}

    .feature-item {{
        display: flex;
        gap: .7rem;
        align-items: flex-start;
        padding: .45rem 0;
        color: #35476f;
        font-size: .87rem;
    }}

    .feature-item b {{
        color: #172554;
    }}

    .stats {{
        display: flex;
        flex-wrap: wrap;
        gap: .8rem;
        margin-top: 1rem;
    }}

    .stat {{
        flex: 1 1 180px;
        background: rgba(20,40,90,.86);
        border: 1px solid rgba(255,255,255,.25);
        color: white;
        padding: 1rem;
        border-radius: 16px;
        box-shadow: 0 8px 22px rgba(30,50,110,.12);
    }}

    .stat strong {{
        display: block;
        font-size: 1rem;
        margin-bottom: .3rem;
    }}

    .stat span {{
        color: #dce7ff;
        font-size: .82rem;
        line-height: 1.5;
    }}

    .small-note {{
        color: #586989;
        font-size: .83rem;
        line-height: 1.5;
    }}

    @media (max-width: 700px) {{
        .hero {{ padding: 1.3rem; }}
        .hero-badge {{ flex: 1 1 100%; }}
        div[data-testid="stForm"] {{ padding: .8rem; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown(
    """
    <div class="hero">
        <h1>🏡 House Price <span class="gradient-word">Predictor</span></h1>
        <p>Estimate the median housing value of a California area
        using machine learning.</p>
        <div class="hero-badges">
            <div class="hero-badge">📊 <b>Random Forest</b><br>Test R² = 0.8141</div>
            <div class="hero-badge">📍 <b>California Housing</b><br>20,640 area records</div>
            <div class="hero-badge">⚡ <b>Instant prediction</b><br>Interactive estimator</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1.25, 0.9], gap="large")

with left:
    st.markdown(
        """
        <div style="color:#172554; font-size:1.45rem; font-weight:800;
                    margin-bottom:.25rem;">
            🎛️ Enter Housing Details
        </div>
        <p class="small-note">
            Enter area-level statistics. The model needs all eight features.
        </p>
        """,
        unsafe_allow_html=True,
    )

    with st.form("housing_form"):
        col_a, col_b = st.columns(2, gap="medium")

        with col_a:
            medinc = st.number_input(
                "💰 Median income", min_value=0.0, value=3.19, step=0.1,
                help="Units of $10,000. A value of 3.19 means about $31,900."
            )
            houseage = st.number_input(
                "🏠 Median house age", min_value=1.0, value=20.0, step=1.0
            )
            averooms = st.number_input(
                "🛏️ Average rooms", min_value=0.1, value=5.0, step=0.5
            )
            avebedrms = st.number_input(
                "🛌 Average bedrooms", min_value=0.1, value=1.0, step=0.1
            )

        with col_b:
            population = st.number_input(
                "👥 Area population", min_value=1.0, value=1000.0, step=100.0
            )
            aveoccup = st.number_input(
                "👨‍👩‍👧 Average occupancy", min_value=0.1, value=3.0, step=0.1
            )
            latitude = st.number_input(
                "📍 Latitude", min_value=32.0, max_value=42.0,
                value=34.0, step=0.1
            )
            longitude = st.number_input(
                "🧭 Longitude", min_value=-125.0, max_value=-114.0,
                value=-118.1, step=0.1
            )

        submitted = st.form_submit_button(
            "✨  Predict House Value",
            use_container_width=True,
        )

    if submitted:
        input_data = pd.DataFrame([{
            "MedInc": medinc,
            "HouseAge": houseage,
            "AveRooms": averooms,
            "AveBedrms": avebedrms,
            "Population": population,
            "AveOccup": aveoccup,
            "Latitude": latitude,
            "Longitude": longitude,
        }])

        prediction = float(model.predict(input_data)[0])
        st.session_state["prediction"] = prediction

with right:
    prediction = st.session_state.get("prediction")

    if prediction is None:
        result_html = """
        <div class="result-card">
            <div class="result-title">🏡 Your estimated value</div>
            <div style="color:#64748b; font-size:1.05rem; margin-top:1rem;">
                Fill in the housing details and select
                <b>Predict House Value</b> to see your result here.
            </div>
            <div class="notice">
                ✅ Area-level estimate, not an individual property's market price.
            </div>
        </div>
        """
    else:
        dollars = prediction * 100000
        result_html = f"""
        <div class="result-card">
            <div class="result-title">📈 Predicted Median House Value</div>
            <div class="result-price">${dollars:,.0f}</div>
            <div class="result-sub">≈ {prediction:.2f} in $100,000s</div>
            <div class="notice">
                <b>✓ Estimate generated successfully</b><br>
                This represents a California housing area's median value.
                The dataset target is capped at approximately $500,000.
            </div>
        </div>
        """

    st.markdown(result_html, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="feature-card">
            <h3 style="margin-top:0;">📘 About the Features</h3>
            <div class="feature-item">💰 <span><b>Median income</b><br>
                Income in units of $10,000</span></div>
            <div class="feature-item">🏠 <span><b>House age</b><br>
                Median age of houses in the area</span></div>
            <div class="feature-item">🛏️ <span><b>Average rooms / bedrooms</b><br>
                Area-level household averages</span></div>
            <div class="feature-item">👥 <span><b>Population / occupancy</b><br>
                Population and average people per household</span></div>
            <div class="feature-item">📍 <span><b>Latitude / longitude</b><br>
                Geographic coordinates of the area</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="stats">
        <div class="stat">
            <strong>🎯 Machine Learning</strong>
            <span>Random Forest with hyperparameter tuning</span>
        </div>
        <div class="stat">
            <strong>🗂️ California Housing Dataset</strong>
            <span>20,640 housing-area records</span>
        </div>
        <div class="stat">
            <strong>📊 Model Performance</strong>
            <span>Test R²: 0.8141<br>MAE: 0.3202 &nbsp; | &nbsp; RMSE: 0.4935</span>
        </div>
    </div>
    <p style="text-align:center;color:#586989;font-size:.8rem;margin-top:1rem;">
        Educational machine-learning demo • Not a real-estate appraisal
    </p>
    """,
    unsafe_allow_html=True,
)
