import urllib
from bs4 import BeautifulSoup

url = "https://www.yahoo.co.jp/"
instance = urllib.request.urlopen(url)
soup = BeautifulSoup(instance,"html.parser")

# cssセレクター(ブラウザの機能)を使って指定した場所のtextを表示する
# nth-childをnth-of-typeに書き換える
# result = soup.select_one("#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-child(1) > article > a > div > div > h1 > span").text
result = soup.select_one("#tabpanelTopics1 > div > div._2jjSS8r_I9Zd6O9NFJtDN- > ul > li:nth-of-type(1) > article > a > div > div > h1 > span").text

print(result)
