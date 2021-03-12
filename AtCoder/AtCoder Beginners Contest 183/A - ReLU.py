# https://atcoder.jp/contests/abc183/tasks/abc183_a

N = int(input())

# nが0以上
# nをそのまま出力する
if n >= 0:
    print(n)

# nが0以下
# 0を出力する
if n < 0:
    n = 0
    print(n)