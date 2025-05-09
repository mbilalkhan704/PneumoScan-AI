from predictors.pneumonia import predict_pneumonia

# Example usage
image_path = "chest_xray/test/PNEUMONIA/person100_bacteria_475.jpeg"
label, prob = predict_pneumonia(image_path)
print(f"Prediction: {label} (Confidence: {prob:.2f})")
