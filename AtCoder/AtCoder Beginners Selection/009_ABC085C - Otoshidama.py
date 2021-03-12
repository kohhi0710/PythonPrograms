# 入力値それぞれにint変換を施し、NとYに代入
N,Y = map(int,input().split())

# ans　3要素の配列　初期値すべて-1
ans = [-1,-1,-1]

# Nの数だけループ
for i in range(N + 1):
    
    # Nからiを引いた数だけループ
    for j in range(N + 1 - i):
        # お札の数だけ計算し、Yと同じ値になったとき
        if i * 1000 + j * 5000 + (N - i - j) * 10000 == Y:
            # ansの配列に値を入れる
            ans = [(N - i - j),j,i]
# ansの全要素をmapでstring型に変換
# →list型に変換
# →区切り文字" "でjoinを使い配列を結合
# →出力
print(" ".join(list(map(str,ans))))