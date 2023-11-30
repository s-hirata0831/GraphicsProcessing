from ultralytics import YOLO

model: YOLO = YOLO(model="yolov8.pt")

result: list = model.predict("https://ultralytics.com/images/bus.jpg",)