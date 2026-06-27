import cv2
from predict import predict_crack

image = cv2.imread("../data/Positive/00001.jpg")   # Use an existing image

label, confidence = predict_crack(image)

print("Prediction:", label)
print("Confidence:", confidence)