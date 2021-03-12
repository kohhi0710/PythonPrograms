import cv2
import numpy as np

filename = "./TestPicture/testsheezoo01.jpg" # Start.pyから見た相対パス

# 白黒で読み込み
img = cv2.imread(filename,0)
# エッジ検出
canny_img = cv2.Canny(img,50,110)

cv2.imwrite('./TestPicture/testsheezoo01_003_1.jpg',img)

canny_img = cv2.Canny(img,999,110)
cv2.imwrite('./TestPicture/testsheezoo01_003_2.jpg',img)

canny_img = cv2.Canny(img,50,999)
cv2.imwrite('./TestPicture/testsheezoo01_003_3.jpg',img)
