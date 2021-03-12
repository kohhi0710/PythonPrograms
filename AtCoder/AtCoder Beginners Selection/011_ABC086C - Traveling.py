# 関数　引数2個
def getDistination(now_pos,next_pos):
    # Max(現在値 - 次の値) - Min(現在値 - 次の値)
    x = max(now_pos[0],next_pos[0]) - min(now_pos[0],next_pos[0])
    y = max(now_pos[1],next_pos[1]) - min(now_pos[1],next_pos[1])
    # xとyを足して返す
    return x + y

N = int(input())
# dict型を宣言
points = {}

# Nだけループ
for i in range(N):
    t,x,y = map(int,input().split())
    # keyにt(移動時間量)の値を入れ、valueにタプルでxとyの座標を入力する
    points[t] = (x,y)

ans = "Yes"
# 現在移動時間量のカウント
now_time = 0
# 現在の座標
now_pos = (0,0)

# pointsに入れたkey値でループ
# key値の各要素にアクセス
for next_time in points.keys():
    # アクセスしたkey値の座標を次の座標として退避
    next_pos = points[next_time]

    # 関数に現在の座標と次の座標を投入し、戻り値を距離として代入
    req_dist = getDistination(now_pos,next_pos)
    # 現在アクセス中のkeyの値から現在のカウント時間を引いた値を代入
    req_time = next_time - now_time

    rem_time = req_time - req_dist

    #rem_timeが0以上　かつ　2の倍数である
    #つまり移動がうまく成立する値である場合
    if rem_time >= 0 and rem_time % 2 == 0:
        #次の時間をカウントに代入
        now_time = next_time
        #次の座標を現在の座標に代入
        now_pos = next_pos
    #不正な値はNoを返す
    else:
        ans = "NO"
        break

print(ans)