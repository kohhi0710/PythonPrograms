# ※※※OpenCVで使うパスに日本語を混ぜると動かないので注意！！！！※※※
# 参考:http://solasyndrome.blog.fc2.com/blog-entry-16.html

import cv2

filename = "./TestPicture/testsheezoo01.jpg" # Start.pyから見た相対パス

# imread(filename,flags):第二引数を以下から選択することで、任意の画像読み込み方法を選択することができる。
# -1 無変換
# 0 グレー
# 1 カラー
# 2 任意の深度
# 3 任意のカラー
img = cv2.imread(filename,0) # グレーに変換
cv2.imwrite('./TestPicture/testsheezoo01_001_1.jpg',img)

img = cv2.imread(filename,-1) # 無変換
cv2.imwrite('./TestPicture/testsheezoo01_001_2.jpg',img)

img = cv2.imread('./TestPicture/testsheezoo01_001_1.jpg',1) # カラーに変換
cv2.imwrite('./TestPicture/testsheezoo01_001_3.jpg',img)