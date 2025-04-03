# YOLO Emotion Detection

This project demonstrates how to use YOLO (You Only Look Once) for object detection on images and videos using the **Ultralytics YOLOv8** model.

## 🚀 Features
- Detect objects in images, videos, and real-time webcam streams
- Save processed images with a custom filename and path
- Save detected objects in videos automatically
- Compatible with **YOLOv11** models

## 📦 Installation
First, install the required dependencies:

```bash
pip install ultralytics opencv-python
```

## 🎯 Usage
### 1️⃣ **Run Detection on an Image**
```python
from ultralytics import YOLO
import cv2

model = YOLO("best_update.pt")

# Image input
image_path = "image.jpg" 
results = model.predict(source=image_path, save=True)


for result in results:
    output_path = "output/input_image.jpg"
    cv2.imwrite(output_path, result.plot()) 
    print(f"Saved detected image at: {output_path}")
```

### 2️⃣ **Run Detection on a Video**
```python
video_path = "video.mp4"  # Replace with your video file path
results = model.predict(source=video_path, save=True)

print("Processed video saved inside 'runs/detect/predict/'")
```

### 3️⃣ **Run Real-Time Detection (Webcam)**
```python
results = model.predict(source=0, show=True)  # 0 for default webcam
```


## 📁 Output
- Processed images are saved at **output/detected_image.jpg**


## 🔥 Notes
- Ensure the **output** folder exists before saving detected images.
- Use `source=0` for real-time detection with a webcam.
- Adjust `model.predict()` parameters for better performance (e.g., confidence threshold, image size, etc.).



