import feedparser
import urllib
from bs4 import BeautifulSoup

# 取得するRSSのURL
RSS_URL = "https://headlines.yahoo.co.jp/rss/trendy-all.xml"

# RSSから取得する
feed = feedparser.parse(RSS_URL)

# 記事の情報をひとつずつ取り出す
for entry in feed.entries:
    # タイトルを出力
    print(entry.title)

    # URLにアクセスし、オブジェクトを作成
    instance = urllib.request.urlopen(url)

    # instanceからHTMLを取り出してBeautifulSoupで扱えるようにパース
    soup = BeautifulSoup(ininstance,"html.parser")

    # タイトル要素を出力
    print(soup.title)