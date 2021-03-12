# ----------------------------------------------------------------------------------------
# global／nonlocalキーワード
# ----------------------------------------------------------------------------------------

# 現在のスコープからグローバルスコープあるいは自分を囲むスコープに存在する変数への再代入を可能にする

name = "hebi.net"

def test():
    # globalキーワードに続けてグローバル変数を記述することで、
    # グローバル変数の値を再代入することができるようになる
    global name
    name = "snake.net" # hebi.net →　snake.net
    print(locals()) 

test() # {}
print(name) # snake.net

# グローバル変数nameを消去後にglobalキーワードを使用しても、問題なく変数を使用できる
del name
test() # {}
print(name) # snake.net

# カウンター関数を作成する関数makecounter
def makecounter():
    n = 0

    def count():
        # 外側のスコープに定義されている変数nを使おうとするとエラーになる
        n += 1
        return n
    return count

counter = makecounter()
# print(counter()) # エラー
# --------------------------------------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 4, in count
# UnboundLocalError: local variable 'n' referenced before assignment
# --------------------------------------------------------------------

def makecounter():
    n = 0

    def count():
        # nonlocalキーワードで外側のスコープの変数nの値を変更できるようにする
        nonlocal n
        n += 1
        return n
    return n

counter = makecounter()
print(counter) # 1
print(counter) # 2
print(counter) # 3