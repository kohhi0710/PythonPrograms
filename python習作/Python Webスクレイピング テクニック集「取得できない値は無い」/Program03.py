#from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

## ブラウザのオプションを格納する変数をもらってくる
#options = Options()

## Headlessモードを有効にする(コメントアウトすると実際にブラウザが立ち上がる)
#options.set_headless(True)

## ブラウザを起動する
#driver = webdriver.Chrome(chrome_options=options)

## ブラウザでアクセスする
#driver.get("file:///Users/admin/Desktop/index.html")

## HTMLを文字コード(UTF-8)に変換してから取得
#html = driver.page_source.encode("utf-8")

## BeautifulSoupで扱えるようにパース
#soup = BeautifulSoup(html,"html.parser")

## idがheikinの要素を表示
#print(soup.select_one("#heikin")