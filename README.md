# 🍎🍌🍇 Fruits Classification using CNN

A Convolutional Neural Network (CNN) built with TensorFlow/Keras to classify different types of fruits from images. The model learns visual patterns — color, texture, and shape — through convolutional and pooling layers to accurately identify fruit categories.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Overview

This project implements an end-to-end image classification pipeline that:

- Preprocesses raw fruit images (resizing, normalization, augmentation)
- Builds a custom CNN architecture using Conv2D, MaxPooling, Flatten, and Dense layers
- Trains and validates the model on a labeled fruit image dataset
- Evaluates performance using accuracy metrics and a confusion matrix
- Exports the trained model for reuse and deployment

The trained `.h5` / `.keras` model is hosted on **Hugging Face** for easy download and inference without retraining.

🔗 **Model on Hugging Face:** [your-username/fruits-classification-cnn](https://huggingface.co/your-username/fruits-classification-cnn)

---

## 🧠 Key Features

| Feature | Description |
|---|---|
| 🖼️ Image Preprocessing | Resizing, rescaling/normalization of pixel values |
| 🔄 Data Augmentation | Rotation, zoom, flip, shift to reduce overfitting and improve generalization |
| 🏗️ Custom CNN Architecture | Multiple Conv2D + MaxPooling blocks followed by Dense layers |
| ⚡ Activation Functions | ReLU (hidden layers), Softmax (output layer for multi-class classification) |
| 🚫 Overfitting Handling | Dropout layers to regularize the network |
| 📊 Evaluation | Accuracy/loss curves and confusion matrix for detailed performance analysis |
| ☁️ Model Hosting | Trained model weights hosted on Hugging Face for easy access |

---

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Deep Learning:** TensorFlow / Keras
- **Image Processing:** OpenCV
- **Numerical Computation:** NumPy
- **Visualization:** Matplotlib
- **Model Hosting:** Hugging Face Hub

---

## 📁 Project Structure

```
Fruits-Classification-CNN/
│
├── dataset/                     # Fruit image dataset (train/test split)
│   ├── train/
│   └── test/
│
├── notebooks/
│   └── fruits_classification.ipynb   # Main notebook with full pipeline
│
├── models/
│   └── fruits_cnn_model.h5      # (or link to Hugging Face if too large for repo)
│
├── images/
│   ├── accuracy_plot.png
│   ├── loss_plot.png
│   └── confusion_matrix.png
│
├── src/
│   ├── preprocess.py            # Image loading, resizing, normalization
│   ├── train.py                 # Model building & training script
│   └── predict.py               # Inference script using saved model
│
├── requirements.txt
├── README.md
└── LICENSE
```

> Update this tree to match your actual repo structure.

---

## 🧩 CNN Architecture

```
Input (Image: 100x100x3)
        │
Conv2D (32 filters, 3x3, ReLU) → MaxPooling2D (2x2)
        │
Conv2D (64 filters, 3x3, ReLU) → MaxPooling2D (2x2)
        │
Conv2D (128 filters, 3x3, ReLU) → MaxPooling2D (2x2)
        │
Flatten
        │
Dense (128, ReLU) → Dropout (0.5)
        │
Dense (num_classes, Softmax)
```

> Adjust filter sizes, layer count, and dropout rate to match your actual model summary.

---

## 📊 Dataset

- **Source:** [Add dataset name/link, e.g., Kaggle Fruits-360 Dataset](#)
- **Classes:** e.g., Apple, Banana, Grape, Mango, Orange, etc.
- **Image Size:** Resized to `100x100` (or your chosen dimensions)
- **Split:** Train / Validation / Test

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Fruits-Classification-CNN.git
   cd Fruits-Classification-CNN
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### `requirements.txt`
```
tensorflow
opencv-python
numpy
matplotlib
scikit-learn
huggingface_hub
```

---

## 🚀 Usage

### 1. Train the model
```bash
python src/train.py
```

### 2. Download the pretrained model from Hugging Face
```python
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="your-username/fruits-classification-cnn",
    filename="fruits_cnn_model.h5"
)
```

### 3. Run inference on a new image
```bash
python src/predict.py --image path/to/fruit_image.jpg
```

Example prediction code:
```python
import tensorflow as tf
import cv2
import numpy as np

model = tf.keras.models.load_model("fruits_cnn_model.h5")

img = cv2.imread("sample.jpg")
img = cv2.resize(img, (100, 100))
img = img / 255.0
img = np.expand_dims(img, axis=0)

prediction = model.predict(img)
class_index = np.argmax(prediction)
print("Predicted class:", class_index)
```

---

## 📈 Results

| Metric | Value |
|---|---|
| Training Accuracy | XX% |
| Validation Accuracy | XX% |
| Test Accuracy | XX% |

**Accuracy & Loss Curves**

![Accuracy Plot](images/accuracy_plot.png)
![Loss Plot](images/loss_plot.png)

**Confusion Matrix**

![Confusion Matrix](images/confusion_matrix.png)

> Replace the placeholder values and screenshots with your actual training results.

---

## 🔮 Future Improvements

- Use transfer learning (e.g., MobileNetV2, EfficientNet) for higher accuracy
- Deploy as a web app using Streamlit or Flask
- Expand dataset with more fruit categories and real-world images
- Add real-time classification via webcam using OpenCV

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check the [issues page](https://github.com/your-username/Fruits-Classification-CNN/issues) or open a pull request.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**Your Name**
- GitHub: https://github.com/Soumendra-Barick/Fruits-Classification-using-CNN
- Hugging Face: https://huggingface.co/soumendrabarick/fruits-classification-cnn/resolve/main/fruits_classification_model.keras

---

⭐ If you found this project useful, consider giving it a star on GitHub!
