from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("best_update.pt")
image_path = "D:\Open cv project\Boy-5.jpg"
results = model.predict(source=image_path,show=True,save=True)#source = "file path" 0-> camera and real time detection 


for result in results:
    output_path = "D:\Open cv project\output-5.jpg" 
    cv2.imwrite(output_path, result.plot())  
    print(f"Saved detected image at: {output_path}")