# Pythonで画像を収集する方法
# https://qiita.com/Kim_Burton/items/3862aace7dacbb87164a

import requests # Http制御用ライブラリ
import urllib.request
import time
import json

def scraping(url,max_page_num,word):

    '''スクレイピング'''
    
    print(f"キーワード\"{word}\"でスクレイピング開始…しばらくお待ち下さい。")

    # ページネーション実装
    # get_page_list関数に引数を入れ、戻り値をpage_list変数に入れる
    page_list = get_page_list(url,max_page_num)
    # 画像URLリスト取得
    # リストオブジェクトの作成
    all_img_src_list = []

    # 取得したpage_listをループで検査
    for page in page_list:
        try:
            # get_img_src_list関数に取り出したデータを入れ、戻り値をimg_src_listに入れる
            img_src_list = get_img_src_list(page)
            # そのデータを上のリストオブジェクトにextendで追加する
            all_img_src_list.extend(img_src_list)
        except:
            # エラーが出たらパス
            pass
    
    # 完成したリストオブジェクトを返す
    print("スクレイピング完了　画像のダウンロードを開始します。")
    print(f"ダウンロードURL数:{len(all_img_src_list)}件  推定ダウンロード完了時間:約{(int)((len(all_img_src_list) * 1) / 60)}分")
    print("------------------------------------------------------------------------")
    return all_img_src_list

def get_img_src_list(url):
    
    '''検索ページにアクセス'''

    # urlをもとに検索ページにアクセスし、webページを取得してオブジェクトを生成
    response = requests.get(url)
    # .textメソッドでhtmlテキスト呼び出し
    webtext = response.text

    # 「<script>__NEXT_DATA__ =」から「;__NEXT_LOADED_PAGES__=」までがダウンロードURL
    start_word = '<script>__NEXT_DATA__ = '
    end_word = ';__NEXT_LOADED_PAGES__='

    # htmlテキストの中からstart_wordを検索し、何文字目にあるかを調べる
    start_num = webtext.find(start_word)
    # 「<script>__NEXT_DATA__ =」 の位置(start_num)からstart_wordの文字数ぶん移動したポイントの値
    # →「<script>__NEXT_DATA__ =」から先のテキストを全て取得する
    webtext_start = webtext[start_num + len(start_word):]
    # htmlテキストの中からend_wordを検索し、何文字目にあるかを調べる
    end_num = webtext_start.find(end_word)
    # 「;__NEXT_LOADED_PAGES__=」以下のテキストをカット
    webtext_all = webtext_start[:end_num]
    # json.loads:文字列(json形式)をディクショナリ形式に変換する
    web_dic = json.loads(webtext_all)

    # 作成したディクショナリ「web_dic」から「algos」値の数だけループ。
    # algosの中から「url」を取り出し、img_src_listに入れる
    img_src_list =  [img['original']['url'] for img in web_dic["props"]["initialProps"]["pageProps"]["algos"]]
 
    # 完成したimg_url_listを返す
    return img_src_list

def get_page_list(url,max_page_num):

    '''ダウンロードURLのリストを取得'''

    # 画像検索のインデックスに与える値(適当な値でOK)
    img_num_per_page = 20
    # ページ数の分だけループし、ダウンロードURLのリストを作成する
    # f以下はパラメータ「b=」に入れる。bは画像検索のインデックスのようなもの。
    page_list = [f'{url}{i * img_num_per_page + 1}' for i in range(max_page_num)]

    # 完成したリストを返す
    return page_list

def download_img(src,dist_path):

    '''画像をダウンロード'''

    time.sleep(1)
    try:
        # ダウンロードURLにアクセス
        # with:C#でいうusingみたいなもん
        with urllib.request.urlopen(src) as data:
            # read():レスポンスの内容を取得(bytes型で取得)
            img = data.read()
            # 指定のパスにimgの値を書き込みする
            with open(dist_path,'wb') as f:
                f.write(img)
                print(f'{dist_path} に画像を保存完了')
    except:
        pass

def main():

    '''yahoo画像検索で画像をダウンロード'''

    # 検索したいワードをコンソールで入力
    print("yahoo画像検索から画像を自動でダウンロードします。")
    print("検索したいワードを入力してEnterキーを押してください。")
    print("検索を複数実行したい場合は「,」で単語を区切ってください。")
    inputword = input("→")
    print("------------------------------------------------------------------------")

    # 検索したいワードをリストで渡す
    search_words = inputword.split(",")

    # enumerate:forループの中でリストやタプルなどのイテラブルオブジェクトの要素と同時に
    #           インデックス番号(カウント、順番)を取得できる。
    # ex)serch_words = ["犬","猫"]のとき、「for num, search_word in enumerate(search_words):」は
    #    num = 0(インデックス番号)、serch_word = "犬"(要素)になる。
    #    2ループ目はnum = 1(インデックス番号)、serch_word = "猫"(要素)になる。
    for num, search_word in enumerate(search_words):
        # f:フォーマット文字列リテラル。fを前置することで、文字列内の{}内の計算式を実行することができる
        #   ここでは、{}内のsearch_wordの値(ex:"犬")を反映させている
        url = f"https://search.yahoo.co.jp/image/search?p={search_word}&ei=UTF-8&b="
        # ページ遷移回数
        # この値*20の件数ぶんダウンロードURLを取得する
        max_page_num = 20
        # スクレイピング関数の戻り値をall_img_src_listに入れる
        # all_img_src_listにはダウンロード用URLが全ておさめられている
        all_img_src_list = scraping(url, max_page_num,search_word)
        all_img_src_list_set = []

        # 画像ダウンロード
        print("ダウンロードを開始します。")
        for i, src in enumerate(all_img_src_list):
            # 比較リストに同じURLが存在しなければダウンロード開始→画像の被りを防ぐ
            if not src in all_img_src_list_set:
                # 指定のフォルダにimage_{num}_{i}.jpgの名前で画像を保存
                download_img(src, f'./DownloadPicture/image_{num}_{i}.jpg') #保存先は適当に変えてください
                # 比較用リストにURLを保存
                all_img_src_list_set.append(src)
        print("ダウンロードが完了しました。")
        print("------------------------------------------------------------------------")
    
        print("何かキーを押して終了してください。")

if __name__ == '__main__':
    main()
