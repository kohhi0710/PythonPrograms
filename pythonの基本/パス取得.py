import os
import sys
import pprint

# カレントディレクトリを取得する
path = os.getcwd()
print("カレントディレクトリ:",path)

# sys.pathを取得する
pprint.pprint(sys.path)
