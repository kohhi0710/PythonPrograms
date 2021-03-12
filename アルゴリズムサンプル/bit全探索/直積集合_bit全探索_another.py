# https://qiita.com/conf8o/items/ba024813b9d9ce934d58

from itertools import product

# 数列Aから1つ以上いくつか選んだとき、その和が3で割り切れるものがあるかどうかを判定
A = [1,4,13,34]
one = [0,1]        # 1
four = [0,1]       # 4
thirteen = [0,1]   # 13
thirtyfour = [0,1] # 34

for bits in product(one,four,thirteen,thirtyfour):
    print("bits      : ",bits)
    a = [x for bit,x in zip(bits,A) if bit == 1]
    if not a : continue

    print("選んだもの: ",a)
    print("和        : ",sum(a))

    if sum(a) % 3 == 0:
        print("Yes")
        exit()