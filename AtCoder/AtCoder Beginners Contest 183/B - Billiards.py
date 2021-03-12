# https://atcoder.jp/contests/abc183/tasks/abc183_b
# 参考資料:https://yamakasa.net/atcoder-abc-183-b/

# 入力値を割り振り
# Sx,Sy = 現在の座標
# Gx,Gy = ゴールの座標
# 求めたいもの = 反射する座標(x,0)のx
Sx,Sy,Gx,Gy = map(int,input().split())

# 傾きの公式　a = Start_y ÷ (Start_x - End_x) 

# 点(Sx,Sy)と点(x,0)を通る直線の傾きをa1とし、
# 点(Gx,Gy)と点(x,0)を通る直線の傾きをa2とすると
# a1 = Sy / Sx - x
# a2 = Gy / Gx - x

#入射角と反射角が等しいことから、a1 = -a2

# (Sy / Sx - x) =  -(Gy / Gx - x)
# x = (Sx * Gy + Sy * Gx) / (Sy + Gy) 
ans = (Sx * Gy + Sy * Gx) / (Sy + Gy)
print(ans)