from predictors.pneumonia import predict_pneumonia

# Example usage
image_path = "sample_images/normal/1.jpeg"
label, prob = predict_pneumonia(image_path)
print(f"Prediction: {label} (Confidence: {prob:.2f})")
