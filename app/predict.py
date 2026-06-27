import tensorflow as tf
import numpy as np
import cv2
from pathlib import Path

# ==========================================
# Load Model
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "best_model.h5"

model = tf.keras.models.load_model(MODEL_PATH)

# ==========================================
# Prediction Function
# ==========================================

def predict_crack(image):

    # Resize Image
    image = cv2.resize(image, (120, 120))

    # Convert BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Normalize
    image = image.astype("float32") / 255.0

    # Add Batch Dimension
    image = np.expand_dims(image, axis=0)

    # Predict
    prediction = model.predict(image, verbose=0)[0][0]

    if prediction >= 0.5:
        label = "Positive (Crack Detected)"
    else:
        label = "Negative (No Crack)"

    confidence = prediction if prediction >= 0.5 else 1 - prediction

    return label, confidence