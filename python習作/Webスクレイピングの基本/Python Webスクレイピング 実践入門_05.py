
import urllib
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time


# アクセスするURL
url = "https://www.yahoo.co.jp/"

# URLにアクセスすると返ってくるhtmlを取得
html = urllib.request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html,"html.parser")

# spanを全て摘出
span = soup.find_all("span")

# print用変数
article_list = []

# forループですべてのspan要素の中からClass = "mkc-stock"となっているものを探す
for tag in span:
    # classの設定がされていない要素は、tag.get("class").pop(0)を行うことができないので、tryでエラー回避
    try:
        # tagの中からclass = "n"のnの文字列を摘出。複数classが設定されている場合があるので
        # get関数では配列で返ってくる。そのため破裂の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
        string_ = tag.get("class").pop(0)

        # fQMqQTGJTbIMxjQwZA2zk _1alzSpTqJzvSVUWqpx82d4と設定されているかどうかを調べる
        if string_ in "fQMqQTGJTbIMxjQwZA2zk _1alzSpTqJzvSVUWqpx82d4":
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            article.list.append(tag.string)
            # 摘出が完了したのでループ終了
            break
    except:
        # エラー時はなにもしない
        pass

for article in article_list:
    print(article)