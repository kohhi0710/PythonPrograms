import urllib
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

time_flag = True

while True:
    # 時間が59分以外のときは58秒間待機する
    # ex)13:15:20→13:16:18
    if datetime.now().minute != 59:
        time.sleep(58)
        continue

    # csvを追記モードでオープン
    f = open("./test/nikkei_heikin.csv","a")
    writer = csv.writer(f,lineterminator = "\n")

    # 59分になったが正確な時間に測定をするために、秒間隔で59秒になるまで抜け出せない
    while datetime.now().second != 59:
        # 00秒ではないため1秒待機
        time.sleep(1)

    # 処理がはやく終わって2回繰り返してしまうので1秒待機する
    time.sleep(1)

    # csvに記述するレコードを作成する
    csv_list = []

    # 現在の時刻を年、月、日、時、分、秒で取得する
    time_ = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # 1カラム目に時間を挿入する
    csv_list.append(time_)

    # アクセスするURL
    url = "http://www.nikkei.com/markets/kabu/"

    # URLにアクセスすると返ってくるhtmlを取得
    html = urllib.request.urlopen(url)

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html,"html.parser")

    # spanを全て摘出
    span = soup.find_all("span")

    # print用変数
    nikkei_heikin = ""

    # forループですべてのspan要素の中からClass = "mkc-stock"となっているものを探す
    for tag in span:
        # classの設定がされていない要素は、tag.get("class").pop(0)を行うことができないので、tryでエラー回避
        try:
            # tagの中からclass = "n"のnの文字列を摘出。複数classが設定されている場合があるので
            # get関数では配列で返ってくる。そのため破裂の関数pop(0)により、配列の一番最初を摘出する
            # <span class="hoge" class="foo">  →   ["hoge","foo"]  →   hoge
            string_ = tag.get("class").pop(0)

            # -stock_pricesと設定されているかどうかを調べる
            if string_ in "mkc-stock_prices":
                # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
                nikkei_heikin = tag.string
                # 摘出が完了したのでループ終了
                break
        except:
            # エラー時はなにもしない
            pass

    print(time_,nikkei_heikin)
    csv_list.append(nikkei_heikin)
    writer.writerow(csv_list)
    f.close()
