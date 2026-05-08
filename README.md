# PneumoScan AI 🩺

A GUI-based deep learning application for the automated detection of pneumonia from chest X-ray images. Designed with accessibility and clinical utility in mind, PneumoScan AI combines a user-friendly interface with a powerful stacked CNN model (MobileNetV2 + DenseNet169), achieving a classification accuracy of **92%**.

## Demo

![App Screenshot Placeholder](https://github.com/mbilalkhan704/PneumoScan-AI/blob/main/Screenshot%20(163).png)

---

## 🧪 Features

- 🧠 **Stacked Deep Learning Model**: Combines MobileNetV2 and DenseNet169 using transfer learning for superior image classification.
- 🖼️ **Image Preprocessing**: Automatic resizing, normalization, and augmentation for training robustness.
- 💻 **GUI Interface**: Built with Tkinter for a seamless user experience.
- 📈 **Real-time Results**: Upload a chest X-ray and receive a diagnosis (NORMAL or PNEUMONIA) with a confidence score.
- 📊 **Evaluation Tools**: Confusion matrix, classification report, and training/validation curve visualizations included.

---

## 📁 Project Structure

PneumoScanAI/  
│  
├── predictors/ # Model and prediction logic  
│ ├── pneumonia_classifier.h5  
│ ├── stacked_model.h5  
│ └── pneumonia.py  
│ └── model.ipynb # Model training notebook  
│  
├── main.py # Simple application  
├── gui.py # GUI application  
├── final_report.pdf # Project Report  
└── README.md


---

## 🛠️ Tech Stack

- **Language**: Python 3.12.4
- **GUI**: Tkinter
- **Deep Learning**: TensorFlow, Keras
- **Image Processing**: OpenCV
- **Evaluation**: scikit-learn, matplotlib, seaborn

---

## 🧠 Model Details

- Input shape: 224x224x3
- Backbone networks: MobileNetV2, DenseNet169
- Layers: Feature maps concatenated, followed by fully connected layers with dropout
- Optimizer: Adam (lr=0.0001)
- Loss Function: Binary Crossentropy
- Accuracy: 92% on test set (624 samples)

---

## How It Works

1. **Launch the App** (`gui.py`)
2. **Upload** a chest X-ray (JPG/PNG)
3. The system will:
   - Preprocess the image
   - Run inference using the trained stacked model
   - Display diagnosis and confidence score in GUI

---

## 📊 Results

- **Accuracy**: 92%
- **Precision/Recall/F1**: Evaluated via scikit-learn's classification report
- **Visualizations**: Training curves and confusion matrix included

---

## Limitations

- Dataset imbalance between NORMAL and PNEUMONIA classes
- Binary classification only (does not detect other lung diseases)

---

## Future Work

- Expand dataset and add multi-class detection
- Integrate attention mechanisms for ROI visualization
- Enable DICOM file support
- Cloud-based deployment for wider accessibility

---

## Acknowledgments

Developed as part of the **Artificial Intelligence course (BSCS-515)** at **University of Karachi (UBIT)**. We thank open-source contributors and platforms like Kaggle, TensorFlow, and Keras for enabling this project.

**Team Members**:
- Muhammad Bilal Khan (Group Leader)
- Hafiz Muhammad Shahrayar
- Haseeb Ahmed
- Muhammad Abdullah
- Muhammad Wasif Raza
- Syed Zawar Hussain

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and distribute it with proper attribution.

