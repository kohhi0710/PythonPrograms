N = int(input())

# Nの分だけinputを実行し、intに変換
s = [int(input()) for i in range(N)]
# 配列をリストにセットし、sを再宣言し代入
# pythonの変数は「データを保管する場所」であり、型は代入する時に決定されデータ自体に保持される
# そのため一度宣言した変数に別の型のデータを入れても問題ない
# set関数(集合型)を使用すると重複する要素は取り除かれる
# set型で配列のオブジェクトを作り、それをさらにlist型に変換している
s = list(set(s))

# 引数reverse = trueで逆順ソート
s.sort(reverse = True)

# lenでリストの要素数を計算
print(len(s))