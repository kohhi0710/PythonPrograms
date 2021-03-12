# ----------------------------------------------------------------------------------------
# 制御構造
# ----------------------------------------------------------------------------------------

# if文/for文/whileがある
# breakで一番内側のループを終了、continueで次の反復を開始
# whileとfor文のelseは、break文が実行されなかった場合にループ処理時に実行される
# (途中でループを終了しないときに限って、最後に何らかの処理を付加したい場合に使用できる)

for n in range(3):
    for m in range(5):
        if m == 3:
            continue
        print("n: " + str(n) + ", m: " + str(m))
# ↓処理結果
# n: 0, m: 0
# n: 0, m: 1
# n: 0, m: 2
# n: 0, m: 4
# n: 1, m: 0
# n: 1, m: 1
# ---省略---

# bはbytes型(バイトストリーム)
b = b'abcdefg'
print(b) # b'abcdefg'
print(type(b)) # <class 'bytes'>
l = len(b)
c = 0

while c < l:
    print(b[c])
    c += 1
# ↓処理結果
# 97
# 98
# 99
# 100
# ---省略---

# ----------------------------------------------------------------------------------------
# 関数
# ----------------------------------------------------------------------------------------

# ラムダ式は単一の式のみからなる無名関数を定義する
# (小規模な処理を、他の関数の引数として渡す場合などに使用する)
# ジェネレーター関数／ジェネレーター式は呼び出されるとジェネレーターオブジェクトを返送する。
# ジェネレーターオブジェクトは、その実行コンテキストを記憶しており、return文ではなくyield文
# を使用して、呼び出し元に何らかの値を返送する。
# その後、制御がジェネレーターオブジェクトに戻ると、直前の状態から実行を継続する。

# 関数定義
def even(n):
    # n % 2 = 0になる値を返す
    # 0は仕様上Falseとなり、そのままでは返せないのでnotをつけてTrueにする
    return not n % 2

l = list(range(5))
# filter関数の引数に関数を渡す(偶数のみをリストから取得)
l2 = list(filter(even,l))
print(l2) # [0, 2, 4]

# 同じことをラムダ式を使用して行う
l3 = list(filter(lambda x: not x % 2,l))
print(l3) # [0, 2, 4]

# ジェネレーター関数定義
def gen(n):
    for m in range(n):
        # return文ではなくyield文で呼び出し側に値を返送する
        yield m

# ジェネレーター関数の利用
for num in gen(3):
    print(num)
# ↓処理結果
# 0
# 1
# 2

# ジェネレーター式
for num in(i + 1 for i in range(3)):
    print(num)
# ↓処理結果
# 1
# 2
# 3

# ラムダ式とジェネレーター式の組み合わせ
g = lambda x:(i + 1 for i in range(x))
h = g(3)
for num in h:
    print(num)
# ↓処理結果
# 1
# 2
# 3

# 関数nextにジェネレーターを渡して、反復を行う
h = g(4)
print(next(h)) # 1

# ジェネレーターgen1に処理を移譲
def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()
    yield 3

for num in gen2():
    print(num)
# ↓処理結果
# 1
# 2
# 3

# rangeオブジェクトに処理を移譲
def gen3():
    yield from range(3)

for num in gen3():
    print(num)
# ↓処理結果
# 0
# 1
# 2

# ----------------------------------------------------------------------------------------
# 例外処理
# ----------------------------------------------------------------------------------------

try:
    # ゼロ除算
    1 / 0

# タプルで複数例外を補足
except(ZeroDivisionError,OverflowError)as exc:
    print(exc)
# その他の例外を補足
except:
    print("trap Exception")
# この例ではelseされない
else:
    print("else")
# クリーンアップ処理
finally:
    print("finally")

# ↓処理結果
# division by zero
# finally

# 例外の送出
# raise [例外オブジェクト1 [from 例外オブジェクト2]] 