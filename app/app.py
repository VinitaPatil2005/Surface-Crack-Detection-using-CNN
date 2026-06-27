import streamlit as st
import cv2
import numpy as np
from PIL import Image
from predict import predict_crack

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Surface Crack Detection",
    layout="centered"
)

st.title("Surface Crack Detection using CNN")

st.write(
    "Upload an image of a concrete surface to detect whether it contains a crack."
)

st.divider()

# ==========================================
# Upload Image
# ==========================================

uploaded_file = st.file_uploader(
    "Choose an Image",
    type=["jpg", "jpeg", "png"]
)

# ==========================================
# Prediction
# ==========================================

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    image = np.array(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    label, confidence = predict_crack(image)

    st.image(
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
        caption="Uploaded Image",
        width=450
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Prediction", label)

    with col2:
        st.metric("Confidence", f"{confidence:.2%}")

    st.progress(float(confidence))

    if "Positive" in label:
        st.error("Crack Detected")
    else:
        st.success("No Crack Detected")

st.divider()

st.caption("Built using TensorFlow, OpenCV and Streamlit")