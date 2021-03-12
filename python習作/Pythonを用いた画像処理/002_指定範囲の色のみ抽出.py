import cv2
import numpy as np

filename = "./TestPicture/testsheezoo01.jpg" # Start.pyから見た相対パス

# カラー読み込み
img = cv2.imread(filename,1)
# 赤と緑でカビみたいな色に変換
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# 取得する色の範囲を指定する
lower_color = np.array([20,50,50])
upper_color = np.array([255,255,255])

# 指定した色に基づいたマスク画像の生成
img_mask = cv2.inRange(hsv,lower_color,upper_color)

# フレーム画像とマスク画像の共通の領域を抽出する
img_color = cv2.bitwise_and(img,img,mask=img_mask)

cv2.imwrite("./TestPicture/testsheezoo01_002.jpg",img_color)