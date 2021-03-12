# https://qiita.com/keitakurita/items/5a31b902db6adfa45a70

def count_up():
    x = 0

    while True:
        yield x
        x += 1

# count_up関数は、呼び出しただけでは何も返さない
# 関数を使うというよりは、「クラスのインスタンスを生成する」という解釈に近い
count_up()

# for文で呼び出すと順番に値を返す
# 呼び出されるたびにxの値をインクリメントして返す
for i in count_up():
    print(i)
    if i == 5:
        break

y = count_up()

# yにcount_upを代入することも可能
for i in y:
    print(i)
    if i == 5:
        break # 0
              # 1
              # 2
              # 3
              # 4
              # 5

# ジェネレーター(yield)は、呼び出されるたびに「行われた処理を記憶する」
# つまり、「ステートを持つ」
for i in y:
    print(i)
    if i == 10:
        # 上のforループで0～5の値を返したので、6～10の値を新たに返している
        break # 6
              # 7
              # 8
              # 9
              # 10

# フィボナッチ数列を計算する関数(returnを用いる場合)
# nの値が小さければ問題ないが、大きくなってくるとスタックがいっぱいになってエラーになる。
def fibonacci_rtn(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# フィボナッチ数列を計算する関数(yieldを用いる場合)
# 直前の2つの数列をステートとして保持することで、スタックを無駄に消費せずに済む
def fibonacci_yld(n):
    a, b = 0,1
    while 1:
        yield b
        a,b = b,a + b

# -----------------------------------------------------------------------------------------------------
# ジェネレーターが活躍する場面は、順々に値を返し、
# ステートを持つ必要があるが、リスト全体を保持する必要がない場面である
# -----------------------------------------------------------------------------------------------------

# パイプライン
# いくつかのジェネレーターを接続して処理を行うアルゴリズム
# 工場でベルトコンベアー式に横から処理を行っていくイメージ
# 下の例は、与えられたリストの偶数要素を3倍にして文字列に変換して返すパイプラン
def even_filter(nums): # 偶数かどうか?
    for num in nums:
        if num % 2 == 0:
            yield num

def multiply_by_three(nums): # 3倍にする
    for num in nums:
        yield num * 3

def convert_to_string(nums): # 文字列に変換
    for num in nums:
        yield "The Number: %s" % num

nums = [1,2,3,4,5,6,7,8,9,10]

pipeline = convert_to_string(multiply_by_three(even_filter(nums)))

for num in pipeline:
    print(num)

# 再帰
# ジェネレーターを再帰的に使って木構造を走査するコード
class Node:
    def __init__(self, data):
        self.data = data
    self.left = None
    self.right = None

def traverse(node):
    if node is not None:
        for x in traverse(node.left):
            yield x

            yield t.dat

            for x in traverse(node.right):
                yield x