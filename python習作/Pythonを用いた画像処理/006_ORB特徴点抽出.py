import cv2
import numpy as np

filename = "./TestPicture/testsheezoo01.jpg" # Start.pyから見た相対パス

img = cv2.imread(filename,1) # 白黒

# ORBを作成
# ORB以外のアルゴリズムでも特徴点を抽出できる
# -----------------------------
# ORB - cv2.ORB_create()
# FAST - cv2.FastFeatureDetector_create()
# AKAZE - cv2.AKAZE_create()
# BRISK - cv2.BRISK_create()
# KAZE - cv2.KAZE_create()
# SIFT - cv2.xfeatures2d.SIFT_create()
# MSER - cv2.MSER_create()
# AgastFeatureDetector - cv2.AgastFeatureDetector_create()
# -----------------------------
detector = cv2.ORB_create()

# 特徴点検出
keypoints = detector.detect(img)

# 画像への特徴点の書き込み
img_orb = cv2.drawKeypoints(img,keypoints,None)

# 出力
cv2.imwrite("./TestPicture/testsheezoo01_006_1.jpg",img_orb)

# 他のアルゴリズム↓
detector = cv2.FastFeatureDetector_create()
keypoints = detector.detect(img)
img_orb = cv2.drawKeypoints(img,keypoints,None)
cv2.imwrite("./TestPicture/testsheezoo01_006_2.jpg",img_orb)

detector = cv2.AKAZE_create()
keypoints = detector.detect(img)
img_orb = cv2.drawKeypoints(img,keypoints,None)
cv2.imwrite("./TestPicture/testsheezoo01_006_3.jpg",img_orb)

detector = cv2.BRISK_create()
keypoints = detector.detect(img)
img_orb = cv2.drawKeypoints(img,keypoints,None)
cv2.imwrite("./TestPicture/testsheezoo01_006_4.jpg",img_orb)

detector = cv2.KAZE_create()
keypoints = detector.detect(img)
img_orb = cv2.drawKeypoints(img,keypoints,None)
cv2.imwrite("./TestPicture/testsheezoo01_006_5.jpg",img_orb)

detector = cv2.xfeatures2d.SIFT_create()
keypoints = detector.detect(img)
img_orb = cv2.drawKeypoints(img,keypoints,None)
cv2.imwrite("./TestPicture/testsheezoo01_006_6.jpg",img_orb)

detector = cv2.MSER_create()
keypoints = detector.detect(img)
img_orb = cv2.drawKeypoints(img,keypoints,None)
cv2.imwrite("./TestPicture/testsheezoo01_006_7.jpg",img_orb)

detector = cv2.AgastFeatureDetector_create()
keypoints = detector.detect(img)
img_orb = cv2.drawKeypoints(img,keypoints,None)
cv2.imwrite("./TestPicture/testsheezoo01_006_8.jpg",img_orb)