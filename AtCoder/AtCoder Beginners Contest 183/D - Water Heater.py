# https://atcoder.jp/contests/abc183/tasks/abc183_d

n,w = map(int,input().split())
# 時刻のリスト 
# DPを用いる
# 制約：0 <= Si < Ti <= 2 * 10^5より
# len(l) = 20001となる
l = [0] * (2 * 10 ** 5 + 1) 

# 人数分だけループ
for i in range(n):
    s,t,p = map(int,input().split())
    # 時刻Siのリストの箇所にP(使用湯量)を与える
    l[s] += p
    # 時刻Tiのリストの箇所にP(使用湯量)を減らす
    l[t] -= p

# 時刻リストの分ループ
for i in range(1,len(l)):
    # 現在時刻に、前回時刻の使用湯量を記録していく
    l[i] += l[i - 1]

# maxでリストの値を探索し、wを超えなければYes、超えたらNo
print("Yes" if max(l) <= w else "No")
