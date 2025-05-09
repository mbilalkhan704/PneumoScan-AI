import cv2
import numpy as np
import os
from tensorflow.keras.models import load_model # type: ignore

# Define the path to the model files inside the 'predictors' folder
MODEL_PATH = os.path.join(os.path.dirname(__file__), "pneumonia_classifier.h5")

# Load the model once (when the module is imported)
loaded_model = load_model(MODEL_PATH)

# Define the prediction function
def predict_pneumonia(image_path):
    """
    Predicts whether an image contains pneumonia or not.

    :param image_path: Path to the image
    :return: Tuple containing the prediction label ("PNEUMONIA" or "NORMAL") 
             and the confidence score
    """
    # Load and process the image
    im = cv2.imread(image_path)
    if im is None:
        raise ValueError(f"Could not read image at {image_path}")
    
    image = cv2.resize(im, (224, 224))
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    
    # Get the prediction
    prob = loaded_model.predict(image)[0][0]
    label = "PNEUMONIA" if prob > 0.5 else "NORMAL"
    
    return label, prob
