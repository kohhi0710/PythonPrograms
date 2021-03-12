import cv2
import numpy as np

filename1 = "./TestPicture/testsheezoo01.jpg" # Start.pyから見た相対パス
filename2 = "./TestPicture/testsheezoo01_004_1.jpg" # Start.pyから見た相対パス

# 白黒で読み込み
img1 = cv2.imread(filename1,1)
img2 = cv2.imread(filename2,1)

# ORB (Oriented FAST and Rotated BRIEF)
detector = cv2.ORB_create()

# 特徴検出
kp1,des1 = detector.detectAndCompute(img1,None)
kp2,des2 = detector.detectAndCompute(img2,None)

# マッチング処理
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)

# 特徴記述子のマッチング
matches = bf.match(des1,des2)

# 距離でソートする
matches = sorted(matches,key = lambda x:x.distance)

distance = 0

for m in matches:
    print(m.distance)
    distance = distance + m.distance

print("マッチング距離：",distance)

# マッチング上位20個の特徴点を線でリンクして画像に書き込む
match_img = cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None,flags=2)

cv2.imwrite("./TestPicture/testsheezoo01_008_1.jpg", match_img)