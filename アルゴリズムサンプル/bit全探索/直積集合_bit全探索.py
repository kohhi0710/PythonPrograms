# https://qiita.com/conf8o/items/ba024813b9d9ce934d58

from itertools import product

# 数列Aから1つ以上いくつか選んだとき、その和が3で割り切れるものがあるかどうかを判定
A = [1,4,13,34]
n = len(A)

# itertools.product() = 直積(デカルト積)を生成する
# ex)2つのリストがあったとき、全てのペアの組み合わせのリストが直積
# ex)直積集合とは、複数の集合に対してそれぞれの要素を一つずつ取り出して組とするときの全パターンを集めたもの
for bits in product([0,1],repeat = n): # repeat:ループ回数
    print("bits      : ",bits)
    a = [x for bit,x in zip(bits,A) if bit == 1]
    if not a : continue

    print("選んだもの: ",a)
    print("和        : ",sum(a))

    if sum(a) % 3 == 0:
        print("Yes")
        exit()