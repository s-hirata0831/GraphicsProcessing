from ultralytics import YOLO
import cv2

# モデル読み込み
model = YOLO(R"C:\Users\hirat\Documents\OpenCV\TeamMission\yolov8n.pt")

# カメラ読み込み
cap = cv2.VideoCapture(0)

while True:
    # カメラから1フレーム読み込み
    ret, frame = cap.read()

    # YOLOv8で物体検出
    results = model(frame, show=False)

    # 結果を表示
    for result in results:
        for xyxy in result.boxes.xyxy:
            cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0, 0, 255), 2)
    cv2.imshow('frame', frame)

    # qキーで終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 後処理
cap.release()
cv2.destroyAllWindows()
