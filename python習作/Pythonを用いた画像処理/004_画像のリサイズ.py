import cv2
import numpy as np

filename = "./TestPicture/testsheezoo01.jpg" # Start.pyから見た相対パス

# 白黒画像で画像を読み込み
img = cv2.imread(filename,1)

# 画像の高さ幅を指定
width,height = 60,60
# 画像をリサイズ
img = cv2.resize(img,(width,height))

cv2.imwrite('./TestPicture/testsheezoo01_004_1.jpg',img)

width,height = 1500,1500
img = cv2.resize(img,(width,height))
cv2.imwrite('./TestPicture/testsheezoo01_004_2.jpg',img)