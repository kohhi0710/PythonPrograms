# -----------------------------------------------------------------------------------------------------
# ジェネレーター
# -----------------------------------------------------------------------------------------------------

# ジェネレーター:「何らかの値を連続的に生成する」反復可能なオブジェクトであり、
# ジェネレーター関数を用いて定義する。ジェネレーターはリストやタプルなどと同様に、
# 反復処理に利用できる（ジェネレーター関数の実際の戻り値は反復可能な「ジェネレーター」オブジェクトになる。

# 単純なジェネレーター
# 「引数に指定された値未満の整数列を返す」反復可能オブジェクトを返す
# まずgen関数の出力が先行し、yieldで返された値が呼び出し元のcntに渡され、print(cnt)される。
# 通常のforループなら呼び出し元に戻るまでにループし尽くすが、yieldすることで一旦戻っている
def gen(n):
    for num in range(n):
        print("generated")
        yield num

for cnt in gen(10):
    print(cnt)

# 無限にフィボナッチ数を生成し続けるジェネレーター
def fibgen():
    n0,n1 = 0,1
    
    # フィボナッチ数列0番目 = 0
    # フィボナッチ数列1番目 = 1
    # フィボナッチ数列2番目 = 1 + 0 = 1
    # 以上からyieldで1周目と2周目はそれぞれ0と1を返す
    yield n0 # fib(0)を返す
    yield n1 # fib(1)を返す

    while True:
        # n0に前回の値を記録、n1に前回の値と次の値を足した値を記録
        n0,n1 = n1,n0 + n1
        # 処理をforループに戻し、メッセージが送られてきたらvに代入し、条件分岐で評価する
        v = yield n1

        if v == "terminate":
            break

fb = fibgen()

# フィボナッチ数の値が50を超えたらジェネレーター関数にメッセージを送り、ループを終了させる
for num in fb:
    if num > 50:
        fb.send("terminate")
    print(num)

# カウンター変数を使う
for cnt in range(10):
    # next:イテレータの先頭から値を取り出す。取り出した値はイテレータから消滅する
    print(next(fb))