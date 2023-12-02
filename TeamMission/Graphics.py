from ultralytics import YOLO
import cv2

# モデル読み込み
model = YOLO(R"C:\Users\hirat\Documents\OpenCV\TeamMission\yolov8n.pt")

# 入力画像
results = model(R'C:\Users\hirat\Documents\OpenCV\TeamMission\100yen.png',save=True) 
