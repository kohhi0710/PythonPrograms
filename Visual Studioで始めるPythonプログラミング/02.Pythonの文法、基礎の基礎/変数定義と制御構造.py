a = 100
print("a = ",a)

# 未定義で変数を使用するとエラーになる。
# print("b = ",b)
# ---------------------------------------- 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'b' is not defined
# ---------------------------------------- 

# type:オブジェクトの型を表示する関数
print("type(a) = ",type(a))

# int型の変数aに文字列[あいうえお]を入れるとstr型になる
a = "あいうえお"
print("a = ",a)
print("type(a) = ",type(a))

# 配列を作成
# 型はlist型になる
a = [1,2,3,4,5,6,7,8,9,10]
print("a = ",a)
print("type(a) = ",type(a))

# ※配列[1,2,3,4,5,6,7,8,9,10]のうち、偶数である値
i = 0
# 配列aの長さ分ループする　ゼロカウントスタート
while i < len(a):
    if not a[i] % 2:
        print(a[i])
    i += 1

# pythonのfor文は、C#のforeachに近い性質を持っている
# 配列aの要素を順番に取り出し、奇数か偶数か調べる
for item in a:
    if not item % 2:
        print("偶数",item)
    else:
        print("奇数",item)

# range:引数は順に「初期値、終端値、差分」
# range(1,11,1)で「範囲1～10、差分1の等差数列」が生成される
# 終端値のみを指定することもできる。(自動的に初期値0、差分1となる)
for item in range(1,11,1):
    if not item % 2:
        print(item)