# https://atcoder.jp/contests/abc184/tasks/abc184_b

N,X = map(int,input().split())
S = input()
for x in S:
    if x == "o":
        X += 1
    else:
        X -= 1 if X >= 1 else 0

print(X)