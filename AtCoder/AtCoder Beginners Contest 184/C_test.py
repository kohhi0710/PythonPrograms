# https://qiita.com/u2dayo/items/f59a6661fc8037414a01#c%E5%95%8F%E9%A1%8Csuper-ryuma

def change(a, b, p):
    # 0～40でループ
    for c in range(K):
        # 0～40でループ
        for d in range(K):
            # a + b == c + d (ex: 20 + 20 == 10 + 30) ナナメ方向への無限移動
            # a - b == c - d (ex: 20 - 20 == 10 - 10)　ナナメ方向への無限移動
            # ||:(絶対値)
            # Abs(a - c) + Abs(b - d) <= 3 (ex: (20 - ) + (20 - ) <= 3) 周囲3マス移動
            if (a + b) == (c + d) or (a - b) == (c - d) or (abs(a - c) + abs(b - d)) <= 3:
                if grid[c][d] == -1: # cdのマス値が-1のとき
                    grid[c][d] = p + 1 # 値を入れる

K = 41
grid = [[-1] * K for _ in range(K)] # -1が41個詰め込まれた配列を41個つくる
# //:切り捨て除算
grid[K // 2][K // 2] = 0 # 配列群の中央を0にする(ex:41*41の配列だと、配列[20,20]がちょうど中央になる)

# ex)K = 3のとき、以下のような配列ができあがる
#    K // 2 = 1(余り1、切り捨て)なので、[1,1]の配列の値を0にする
# -1 -1 -1
# -1  0 -1
# -1 -1 -1

# 0～9でループ　10手まで検証可
for i in range(10):
    # 0～40でループ
    for a in range(K):
        # 0～40でループ
        for b in range(K):
            # 中央ポイントをみつけ、その時のループの値をchange関数に入れる
            if grid[a][b] == i:
                change(a, b, i)
    import copy
    grid2 = copy.deepcopy(grid)
    print("--------------------------------------------" +str(i + 1)+ "手目---------------------------------")
    a = 0
    for c2 in range(K):
        a = 0
        for d2 in range(K):
            if grid2[c2][d2] == -1: 
                    grid2[c2][d2] = " "
                    a += 1
    if a > 0:
        for row2 in grid2:
            print(*row2)
        print("-------------------------------------------------------------------------------------------------")

print("--------------------------------------------ラスト---------------------------------")
for row in grid:
    print(*row)