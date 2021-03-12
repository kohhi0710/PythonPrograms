import urllib
from bs4 import BeautifulSoup

# アクセスするURL
url = "http://www.nikkei.com/markets/kabu/"

# アクセス
html = urllib.request.urlopen(url)

# BeautifulSoupで扱う
soup = BeautifulSoup(html,"html.parser")

# タイトルを出力
print(soup.title.string)
