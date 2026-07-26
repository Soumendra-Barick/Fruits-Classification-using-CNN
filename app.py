import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os
import urllib.request


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="FreshCheck AI",
    page_icon="🍏",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(160deg, #f3faf3 0%, #fdfdf8 45%, #fff8f0 100%);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    footer {
        visibility: hidden;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #14532d 0%, #166534 100%);
    }

    section[data-testid="stSidebar"] * {
        color: #ecfdf5 !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.15);
    }

    .fc-hero {
        background: linear-gradient(120deg, #14532d 0%, #15803d 50%, #4d7c0f 100%);
        padding: 52px 40px;
        border-radius: 24px;
        text-align: center;
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 24px 48px -18px rgba(20, 83, 45, 0.45);
    }

    .fc-hero::before {
        content: "";
        position: absolute;
        top: -70px;
        right: -70px;
        width: 240px;
        height: 240px;
        background: radial-gradient(
            circle,
            rgba(190,242,100,0.35) 0%,
            transparent 70%
        );
        border-radius: 50%;
    }

    .fc-hero::after {
        content: "";
        position: absolute;
        bottom: -90px;
        left: -50px;
        width: 240px;
        height: 240px;
        background: radial-gradient(
            circle,
            rgba(251,146,60,0.30) 0%,
            transparent 70%
        );
        border-radius: 50%;
    }

    .fc-hero h1 {
        color: #ffffff;
        font-size: 48px;
        font-weight: 800;
        letter-spacing: -1px;
        margin: 0 0 10px 0;
        position: relative;
        z-index: 1;
    }

    .fc-hero p {
        color: #dcfce7;
        font-size: 18px;
        margin: 0;
        position: relative;
        z-index: 1;
    }

    .fc-badge {
        display: inline-block;
        margin-top: 18px;
        padding: 6px 16px;
        background: rgba(255,255,255,0.14);
        border: 1px solid rgba(255,255,255,0.25);
        border-radius: 999px;
        color: #f0fdf4;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.3px;
        position: relative;
        z-index: 1;
    }

    .fc-section-title {
        color: #14532d;
        font-size: 22px;
        font-weight: 800;
        margin: 8px 0 4px 0;
    }

    .fc-section-sub {
        color: #6b7280;
        font-size: 14px;
        margin-bottom: 16px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px !important;
        border: 1px solid #dcfce7 !important;
        box-shadow: 0 8px 22px -14px rgba(20, 83, 45, 0.18);
        background: #ffffff;
    }

    [data-testid="stFileUploaderDropzone"] {
        background: #f0fdf4;
        border: 2px dashed #86efac;
        border-radius: 16px;
    }

    [data-testid="stFileUploaderDropzone"]:hover {
        border-color: #16a34a;
        background: #dcfce7;
    }

    div.stButton > button {
        background: linear-gradient(
            135deg,
            #16a34a 0%,
            #15803d 100%
        );
        color: white;
        font-weight: 700;
        font-size: 16px;
        border: none;
        border-radius: 12px;
        padding: 0.7rem 1.2rem;
        box-shadow: 0 6px 16px -6px rgba(21, 128, 61, 0.55);
        transition: transform 0.15s ease,
                    box-shadow 0.15s ease;
    }

    div.stButton > button:hover {
        background: linear-gradient(
            135deg,
            #15803d 0%,
            #14532d 100%
        );
        transform: translateY(-2px);
        color: white;
    }

    div.stButton > button:focus {
        outline: none;
        box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.3);
    }

    [data-testid="stMetric"] {
        background: #f0fdf4;
        border: 1px solid #dcfce7;
        border-radius: 14px;
        padding: 14px 16px;
    }

    [data-testid="stMetricValue"] {
        color: #14532d;
        font-weight: 800;
    }

    div[data-testid="stProgress"] > div > div {
        background: linear-gradient(
            90deg,
            #bef264 0%,
            #16a34a 100%
        );
        border-radius: 8px;
    }

    div[data-testid="stProgress"] > div {
        background-color: #e5e7eb;
        border-radius: 8px;
    }

    div[data-testid="stAlert"] {
        border-radius: 14px;
        border: none;
    }

    div[data-testid="stImage"] img {
        border-radius: 14px;
        box-shadow: 0 10px 24px -12px rgba(20, 83, 45, 0.25);
    }

    button[data-baseweb="tab"] {
        font-weight: 600;
        color: #4b5563;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #15803d;
    }

    div[data-baseweb="tab-highlight"] {
        background-color: #15803d !important;
    }

    hr {
        border-color: #dcfce7;
    }

    .fc-footer {
        text-align: center;
        color: #4b5563;
        padding: 26px 0 6px 0;
        margin-top: 30px;
        border-top: 1px solid #dcfce7;
        line-height: 1.9;
        font-size: 14px;
    }

    .fc-result-fresh {
        background: linear-gradient(
            135deg,
            #f0fdf4 0%,
            #dcfce7 100%
        );
        border: 1px solid #86efac;
        border-radius: 16px;
        padding: 20px 24px;
        text-align: center;
    }

    .fc-result-rotten {
        background: linear-gradient(
            135deg,
            #fff7ed 0%,
            #fee2e2 100%
        );
        border: 1px solid #fca5a5;
        border-radius: 16px;
        padding: 20px 24px;
        text-align: center;
    }

    .fc-result-label {
        font-size: 26px;
        font-weight: 800;
        margin: 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL CONFIGURATION
# ============================================================

IMG_HEIGHT = 224
IMG_WIDTH = 224

MODEL_FILENAME = "fruits_classification_model.keras"

MODEL_URL = (
    "https://huggingface.co/"
    "soumendrabarick/fruits-classification-cnn/"
    "resolve/main/fruits_classification_model.keras"
)


# ============================================================
# DOWNLOAD MODEL FROM HUGGING FACE
# ============================================================

@st.cache_resource
def download_and_load_model():

    # Check if model already exists locally
    if not os.path.exists(MODEL_FILENAME):

        with st.spinner(
            "⏳ Downloading CNN model from Hugging Face..."
        ):

            urllib.request.urlretrieve(
                MODEL_URL,
                MODEL_FILENAME
            )

    # Load the downloaded model
    model = tf.keras.models.load_model(
        MODEL_FILENAME
    )

    return model


# ============================================================
# LOAD MODEL
# ============================================================

try:

    model = download_and_load_model()

except Exception as e:

    st.error(
        "❌ Unable to load the CNN model."
    )

    st.write(
        "Please check that your Hugging Face model URL "
        "is correct and publicly accessible."
    )

    st.code(str(e))

    st.stop()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🍏 FreshCheck AI")

    st.write(
        "Upload a fruit image and our CNN model will "
        "determine whether the fruit is **Fresh** or **Rotten**."
    )

    st.divider()

    st.subheader("🧠 Model Info")

    st.write(
        "**Model:** Convolutional Neural Network"
    )

    st.write(
        "**Framework:** TensorFlow / Keras"
    )

    st.write(
        "**Input Size:** 224 × 224"
    )

    st.write(
        "**Task:** Fresh vs Rotten"
    )

    st.write(
        "**Model Hosting:** Hugging Face"
    )

    st.divider()

    st.subheader("📋 How to Use")

    st.write(
        "1. Upload a fruit image.\n"
        "2. Preview the image.\n"
        "3. Click **Analyze Fruit**.\n"
        "4. View the Fresh/Rotten result.\n"
        "5. Check the confidence score."
    )


# ============================================================
# HERO HEADER
# ============================================================

st.markdown(
    """
    <div class="fc-hero">
        <h1>🍏 FreshCheck AI</h1>
        <p>AI-powered fresh vs. rotten fruit classification, in seconds.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption("Powered by a CNN · TensorFlow / Keras")


# ============================================================
# UPLOAD SECTION
# ============================================================

st.markdown(
    '<div class="fc-section-title">'
    '📤 Upload a Fruit Image'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="fc-section-sub">'
    'JPG or PNG. The model works best with a clear, '
    'well-lit photo of a single fruit.'
    '</div>',
    unsafe_allow_html=True
)


with st.container(border=True):

    uploaded_file = st.file_uploader(
        "Choose a fruit image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )


# ============================================================
# IF IMAGE IS UPLOADED
# ============================================================

if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    st.write("")

    image_col, prediction_col = st.columns(
        [1, 1],
        gap="large"
    )


    # ========================================================
    # IMAGE PREVIEW
    # ========================================================

    with image_col:

        with st.container(border=True):

            st.subheader(
                "🖼️ Image Preview"
            )

            st.image(
                image,
                caption="Uploaded Fruit Image",
                use_container_width=True
            )


    # ========================================================
    # PREDICTION AREA
    # ========================================================

    with prediction_col:

        with st.container(border=True):

            st.subheader(
                "🤖 Freshness Analysis"
            )

            st.write(
                "Click the button below to analyze the fruit."
            )

            analyze_button = st.button(
                "🔍 Analyze Fruit",
                use_container_width=True
            )


            if analyze_button:

                with st.spinner(
                    "🧠 CNN is analyzing the fruit..."
                ):

                    # Resize image
                    resized_image = image.resize(
                        (IMG_WIDTH, IMG_HEIGHT)
                    )

                    # Convert to NumPy array
                    img_array = np.array(
                        resized_image,
                        dtype=np.float32
                    )

                    # Normalize
                    img_array = img_array / 255.0

                    # Add batch dimension
                    img_array = np.expand_dims(
                        img_array,
                        axis=0
                    )

                    # Model prediction
                    prediction = model.predict(
                        img_array,
                        verbose=0
                    )

                    probability = float(
                        prediction[0][0]
                    )


                    # ====================================================
                    # CLASSIFICATION
                    # ====================================================
                    # Assumption:
                    # 0 = Fresh
                    # 1 = Rotten
                    #
                    # If your training dataset uses the opposite
                    # class order, this logic must be reversed.

                    if probability >= 0.5:

                        predicted_class = "Rotten"

                        confidence = probability

                    else:

                        predicted_class = "Fresh"

                        confidence = 1 - probability


                st.write("")


                # ====================================================
                # RESULT
                # ====================================================

                if predicted_class == "Fresh":

                    st.markdown(
                        '<div class="fc-result-fresh">'
                        '<p class="fc-result-label">'
                        '🟢 Fresh'
                        '</p>'
                        '</div>',
                        unsafe_allow_html=True
                    )

                else:

                    st.markdown(
                        '<div class="fc-result-rotten">'
                        '<p class="fc-result-label">'
                        '🔴 Rotten'
                        '</p>'
                        '</div>',
                        unsafe_allow_html=True
                    )


                st.write("")


                # ====================================================
                # METRICS
                # ====================================================

                m1, m2 = st.columns(2)


                with m1:

                    st.metric(
                        label="🍎 Fruit Condition",
                        value=predicted_class
                    )


                with m2:

                    st.metric(
                        label="🎯 Confidence",
                        value=f"{confidence * 100:.2f}%"
                    )


                # ====================================================
                # PROGRESS
                # ====================================================

                st.write(
                    "**Confidence Score**"
                )

                st.progress(
                    confidence
                )


                # ====================================================
                # CONFIDENCE MESSAGE
                # ====================================================

                if confidence >= 0.90:

                    st.success(
                        f"The model is highly confident "
                        f"that the fruit is "
                        f"**{predicted_class}**."
                    )

                elif confidence >= 0.70:

                    st.info(
                        f"The model predicts the fruit is "
                        f"**{predicted_class}** "
                        f"with good confidence."
                    )

                else:

                    st.warning(
                        f"The model predicts "
                        f"**{predicted_class}**, "
                        f"but confidence is relatively low."
                    )


# ============================================================
# ABOUT SECTION
# ============================================================

st.divider()

st.markdown(
    '<div class="fc-section-title">'
    '📌 About This Project'
    '</div>',
    unsafe_allow_html=True
)


a1, a2, a3 = st.columns(
    3,
    gap="large"
)


with a1:

    with st.container(border=True):

        st.markdown(
            "#### 🧠 CNN Model"
        )

        st.write(
            "A Convolutional Neural Network learns "
            "visual patterns from fruit images."
        )


with a2:

    with st.container(border=True):

        st.markdown(
            "#### 🔍 Image Processing"
        )

        st.write(
            "Images are resized to 224 × 224 pixels "
            "and normalized before prediction."
        )


with a3:

    with st.container(border=True):

        st.markdown(
            "#### 🍎 Classification"
        )

        st.write(
            "The model classifies the fruit condition "
            "as either Fresh or Rotten."
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="fc-footer">
        🍏 <b>FreshCheck AI</b><br>
        Fresh vs Rotten Fruit Classification using CNN<br>
        Built with Python, TensorFlow, Keras and Streamlit
    </div>
    """,
    unsafe_allow_html=True
)