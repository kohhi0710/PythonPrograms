# https://atcoder.jp/contests/abc184/tasks/abc184_c
# https://qiita.com/u2dayo/items/f59a6661fc8037414a01#c%E5%95%8F%E9%A1%8Csuper-ryuma

def solve():
    # 0手。サンプルにあるので忘れずに記述する
    # スタートとゴールが同じとき
    if a == c and b == d:
        return 0

    # 1手。問題文の条件通りに記述
    if a + b == c + d: # ナナメ移動
        return 1
    if a - b == c - d: # ナナメ移動
        return 1
    if abs(a - c) + abs(b - d) <= 3: # 中心点から距離3以内のマンハッタン距離
        return 1

    # 2手

    # 〇超竜馬移動を2手(上下左右に1マス移動を3回×2＝合計6回移動可能)
    # →「マンハッタン距離」が6以下なら2手で移動可能
    # マンハッタン距離:|始点x - 終点x| + |始点y - 終点y|
    if abs(a - c) + abs(b - d) <= 6:
        return 2

    # 〇ナナメ移動を2手
    # この場合の移動距離の変化(移動量をkとする)は、
    # x座標が+k、y座標が+k(右上)
    # x座標が+k、y座標が-k(右下)
    # x座標が-k、y座標が+k(左上)
    # x座標が-k、y座標が-k(左下)
    # これを2回繰り返すので、x座標とy座標の総和は+2k、0、-2kのどれかとなる。
    # →変化量は全て偶数となるので、奇数の変化量でたどり着くマスには絶対に止まれないことがわかる。
    # →変化量の和が偶数になるマスであれば、どんなに遠いマスでも2手でたどり着ける

    # %の優先順位は高いので、左辺の足し算を()で囲む
    if(abs(a - c) + abs(b - d)) % 2 == 0: # 2で割った余りが0
        return 2

    # 〇ナナメ移動1手と、超竜馬移動1手
    # →ナナメ移動1手後のマスからマンハッタン距離3以内であると考える
    # 問題文より、ナナメ移動でいけるマスは
    # (a + b) = (c + d)、(a - b) = (c - d)
    # 移項すると、
    # →(a + b) - (c + d) = 0
    # →(a - b) - (c - d) = 0
    # これは、ナナメ移動1手分の値となる。
    # このことから計算結果が0～3の範囲で動くとき、ナナメ移動1手と超竜馬移動1手であるといえる
    if abs((a + b) - (c + d)) <= 3:
        return 2
    if abs((a - b) - (c - d)) <= 3:
        return 2

    # 0～2手で移動できないとき
    # 基本的に度外視
    return 3

a,b = map(int,input().split())
c,d = map(int,input().split())

print(solve())



