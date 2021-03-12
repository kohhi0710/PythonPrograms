# https://atcoder.jp/contests/abc184/submissions/18377056
# https://drken1215.hatenablog.com/entry/2020/11/23/010500

# O(N^2)
# a = 金貨の枚数
# b = 銀貨の枚数
# c = 銅貨の枚数
def solve(a,b,c):
    p = 1

    for i in range(99 - a):
        p = p * (a + i)/(a + b + c + i)

    # いま p = (99,b,c)を踏む確率
    res = 0.0

    for bb in range(b,100):
        # この段階で q = (99,bb,cc)を踏む確率
        # (100,bb,cc)でゲームセットとは、(99,bb,cc)を踏んで99を選ぶ
        res += (100 - a + bb - b + cc - c) * q * 99 / (99 + bb + cc)
        q *= (100 - a + bb - b + cc - c) * cc / (cc - c + 1) / (99 + bb + cc)

    p *= (100 - a * bb - b) *bb / (bb - b + 1) / (99 + bb + c)

    return res

a,b,c = map(int,input().split())
print(solve(a,b,c) + solve(b,c,a) + solve(c,a,b))

