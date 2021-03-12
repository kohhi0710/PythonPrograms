# ----------------------------------------------------------------------------------------
# 組み込み関数
# ----------------------------------------------------------------------------------------

# all:全ての要素が真と評価されたらTrueを、そうでなければFalseを返す
# 　　(反復可能オブジェクトが空の場合はTrue)
# any:全ての要素のいずれかが真と評価されたらTrueを、全てが偽と評価されたらFalseを返す
#     (反復可能オブジェクトが空の場合はFalse)
# filter:第一引数に渡した関数で、各要素を評価し、その結果が真となる要素からなるイテレータを返送する
# len:要素数を返す
# map:第一引数に渡した関数を各要素に適用するようなイテレータを返送する
# reversed:要素を逆順にするイテレータを返送する
# sorted:各要素をソートした結果を格納する新たなリストを返送する(元の反復可能オブジェクトは変更されない)
#        ソートに使用する関数も指定可能
# sum:各要素の総和を計算する
# zip:引数に渡した複数の反復可能オブジェクトの各要素を組み合わせたイテレータを返送する

print(all([0,1,2])) # False ※0はFalse判定のため
print(all([1,2,3])) # True
print(all([])) # True

print(any([0,1,2])) # True
print(any([None, True, False])) # True
print(any([])) # False

print(list(filter(lambda x: x % 2 == 0,list(range(5))))) # [0, 2, 4] ※偶数を抽出

print(len(list(range(10)))) # 10 ※10要素からなるリストの要素数

print(list(map(lambda x: x * x,list(range(5))))) # [0, 1, 4, 9, 16] ※各要素を2乗したリスト

print(list(reversed(range(5)))) # [4, 3, 2, 1, 0]

print(sum([1,2,3,4,5,6,7,8,9,10])) # 55

print(list(zip([1,2,3],["a","b","c","d","e"]))) # [(1, 'a'), (2, 'b'), (3, 'c')]

# ----------------------------------------------------------------------------------------
# 文字列関連の組み込み関数
# ----------------------------------------------------------------------------------------

# chr:指定した引数をUnicodeコードポイントとするUnicode文字を返す
# ord:指定した文字のUnicodeコードポイントを返す
# eval:引数に渡した文字列をpython式として解析/評価する
# exec:引数に渡した文字列を一連のpython文として解析/実行する

print(ord("ほ")) # 12411

print(chr(12411)) # ほ

print(hex(12411)) # 0x307b

print(chr(0x307b)) # ほ

# 乱数を利用
import random

# 1/2でTrueかFalse
flag = random.randint(0,9) % 2
print(flag)

# flagがTrueならsnake.net、falseならpoison snake
print(eval('"snake.net" if flag else "poison snake"'))

# エラー、組み込み関数evalでは関数を評価できない
# print(eval('def foo(): print("hello")'))

# 組み込み関数execではこれを評価できる
exec('def foo(): print("execで関数を定義したよ")')
foo() # execで関数を定義したよ
