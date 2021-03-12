import cv2
import numpy as np

filename = "./TestPicture/testsheezoo01.jpg" # Start.pyから見た相対パス
img = cv2.imread(filename,0) # 白黒

# 画像サイズの取得(縦、横)
size = tuple([img.shape[1],img.shape[0]])

# 画像の中心位置(x,y)
center = tuple([int(size[0]/2),int(size[1]/2)])

# 回転させたい角度(正の値は半時計回り)
angle = 180.0

# 拡大比率
scale = 1.0

# 回転変換行列の算出
rot_matrix = cv2.getRotationMatrix2D(center,angle,scale)

# アフィン変換
rot_img = cv2.warpAffine(img, rot_matrix, size, flags=cv2.INTER_CUBIC)

# ORB (Oriented FAST and Rotated BRIEF)
detector = cv2.ORB_create()

# 特徴検出
kp1, des1 = detector.detectAndCompute(img, None)
kp2, des2 = detector.detectAndCompute(rot_img, None)

# マッチング処理
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

# マッチング上位20個の特徴点を線でリンクして画像に書き込む
match_img = cv2.drawMatches(img, kp1, rot_img, kp2, matches[:20], None, flags=2)

cv2.imwrite("./TestPicture/testsheezoo01_007_1.jpg", match_img)