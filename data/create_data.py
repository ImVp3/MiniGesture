"""
Bước 1. Đổi các biến : label (nhãn cần thu thập dữ liệu), farmer (tên người thực hiện)
Bước 2. Chạy code
Bước 3. Xem ảnh mẫu trong các folder data để xem dáng tay
Bước 4. Sau khi thực hiện dáng tay xong thì ấn phím 'r' để bắt đầu record. Sau khi record đủ 200 ảnh thì code tự exit.
        Lưu ý: xoay  cổ tay hoặc di chuyển tay một chút để tạo sự đa dạng cho dữ liệu
Bước 5: commit
Bước 6: nhắn vào nhóm "Đã xong"
"""

import math
import os

import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
offset = 20
imgSize = 200

# Change only here
label = "up"  # left / right / up / stop
farmer = "vp4"  # Replace by your NAME
# End changeable Section

record = False
counter = 0
Max = 0
while True:
    success, img = cap.read( )
    if not success:
        print("Error: can not get image!!")
        break
    img = cv2.flip(img, 1)
    hand, img = detector.findHands(img,draw=False)
    if hand:
        hand = hand[0]
        x, y, w, h = hand['bbox']
        ratio = h/w
        if ratio > 1:
            padding = (h - w)/2
            imgCrop = img[y - offset: y + h + offset, x - math.ceil(padding) - offset: x + w + math.floor(padding) + offset]
        else:
            padding = (w - h)/2
            imgCrop = img[y - math.ceil(padding) - offset: y + h + math.floor(padding) + offset, x - offset: x + w + offset]
        imgCrop = cv2.flip(imgCrop, 1)

        if imgCrop is not None and imgCrop.shape[0] * imgCrop.shape[1] != 0:
            imgCrop = cv2.resize(imgCrop, (200, 200))
            cv2.imshow("Cropped Image", imgCrop)
            if record:
                path = os.path.join(os.path.dirname(__file__), label, f"{farmer}-{label}-{counter}.jpg")
                print(path)
                cv2.imwrite(path, imgCrop)
                counter += 1
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord("e") or counter >= 100:
        exit(0)
    if cv2.waitKey(1) == ord("r"):
        record = True
