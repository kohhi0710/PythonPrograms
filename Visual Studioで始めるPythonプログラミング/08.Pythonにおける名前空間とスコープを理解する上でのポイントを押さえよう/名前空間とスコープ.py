# 組み込み関数listを使ってリストを作成
l = list(range(1,10))
print(l) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 変数listに整数10を代入
list = 10
print(list) # 10

# これはエラーとなる
# listに10を代入したので、rangeの呼び出しが失敗している
# l = list(range(1,10)) 
# ----------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'int' object is not callable
# ----------------------------------------

# ↑はなぜか？
# 組み込み関数listの名前と被る名前の変数listを作成したため、
# エラー箇所のlistでは変数としてのlistが優先された(組み込み関数listが隠蔽された)のでrangeが適用されなかった

# 変数listを名前空間から削除
# これで組み込み関数のlistが使えるようになる
del list
l = list(range(1,10))
print(l) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ローカルスコープとは、現在実行しているコードを含む最小範囲のブロックのこと
# pythonでは関数定義やクラス定義では新たなスコープを生成するが、if文やfor文では生成されない
# なので、ifやfor文の途中で関数を定義したのちブロックを抜けても、その関数は引き続き使うことができる
def test(x):
    if x > 60:
        msg = "pass" # ifブロックで変数msgを定義
    else:
        msg = "fail"
    
    #if文を抜けてもmsgは生きているので使用可能
    print(msg) # pass or fail

# pythonでは、名前空間は辞書として実装され、そこに名前とオブジェクトの対が保存される。
# そして、何らかの名前を検索する際にはローカルスコープから組み込み名前空間へと向かいながら、
# 個々のスコープに対応する名前空間にその名前が存在しているかを検索している