# -----------------------------------------------------------------------------------------------------
# 関数
# -----------------------------------------------------------------------------------------------------

# 関数を定義
def hello(to):
    print("hello {0}".format(to))

# 関数を使う
hello("Satoshi") # hello Satoshi

# 関数のデリゲート
greet = hello
greet("Satoshi") # hello Satoshi

# -----------------------------------------------------------------------------------------------------
# 関数の引数
# -----------------------------------------------------------------------------------------------------

# aとbを計算する関数 ex)a + b
# デフォルトで第三引数に「+」が設定されている
def calc(a,b,op = "+"):
    if op not in "+-*/":
        return
    print(eval("{0} {1} {2}".format(a,op,b))) # evalで文字列を計算式判定し、計算実行

# 第三引数を省略
calc(1,1) # 2

# 第三引数に「-」を設定
calc(1,2,"-") # -1

# 引数の入力は通常順番に割り当てられていくが、キーワード引数を指定すると
# 任意の順番で引数を割り当てられる
calc(1,op = "*",b = 0.5) # 0.5

# キーワード引数と位置指定引数を混在させて関数を呼び出す場合には、
# キーワード引数よりも先に位置指定引数を指定する必要がある。

# 位置指定引数をキーワード引数より後に指定するとエラー
# calc(op = "*",2,3)
# ----------------------------------------------------------------
#  File "<stdin>", line 1
# SyntaxError: positional argument follows keyword argument
# ----------------------------------------------------------------

# デフォルト値を持つのは第三引数のみ、引数bの値を指定していないのでエラー
# calc(1,op = "-")
# ----------------------------------------------------------------
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: calc() missing 1 required positional argument: 'b'
# ----------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
# タプルで可変数個の引数を受け取る
# -----------------------------------------------------------------------------------------------------

# 第三引数以降は、タプルargsに受け取る
# タプルパラメータ名の前に「*」をつける。
# パラメータ名を「args」とするのが通例
def foo(a,b,*args):
    print("タプルargsを含んでいます。")

    for arg in args:
        print(arg)

foo(1,2,100,["りんご","ぶどう"]) # タプルargsを含んでいます。
                                 # 100
                                 # ['りんご', 'ぶどう']

# -----------------------------------------------------------------------------------------------------
# 辞書で可変数個の引数を受け取る
# -----------------------------------------------------------------------------------------------------

# 辞書で受け取る場合、パラメータ前に「**」を設置する
# パラメータ名を「kwargs」とするのが通例
def bar (a = "foo",b = "bar",**kwargs):
    print("キーワードargsを含んでいます。")

    # 辞書に対してitemsメソッドでキー/値の組を取り出し、k,vにそれぞれ代入している
    for k,v in kwargs.items():
        print("{0}:{1}".format(k,v))

# 引数aとbはデフォルト値が設定されているため、未入力の場合は省略される
# 引数cとdは両方ともkwargsに渡される
bar(c = "hoge",d = "huga") # キーワードargsを含んでいます。
                           # c:hoge
                           # d:huga

# -----------------------------------------------------------------------------------------------------
# タプルや辞書の値を展開して関数に渡す
# -----------------------------------------------------------------------------------------------------

# タプルや辞書の内容を展開して、関数に渡したいというときには
# 「*」や「**」を関数呼び出し側で利用する

# タプルを渡す
t = (1,2)
calc(*t,"/") # 0.5

# 辞書を渡す
d = {"a":"foo","b":"bar"}
bar(**d,c = "hoge",d = "huga") # キーワードargsを含んでいます。
                               # c:hoge
                               # d:huga