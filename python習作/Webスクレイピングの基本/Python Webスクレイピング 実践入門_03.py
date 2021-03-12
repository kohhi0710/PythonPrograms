import urllib
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/markets/kabu/"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,"html.parser")

# span要素を全て摘出する
# →すべてのspan要素が配列に入って返される
# →[<span class="m-wficon triDown"></span>, <span class="l-h...
span = soup.find_all("span")

# print時のエラーにならないように最初に宣言
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
        if string_ in "mlc-stock_prices":
            # mkc-stock_pricesが設定されているのでtagで囲まれた文字列を.stringであぶり出します
            nikkei_heikin = tag.string
            # 摘出が完了したのでループ終了
            break
    except:
        # エラー時はなにもしない
        pass
# 摘出した日経平均株価を出力
print(nikkei_heikin)