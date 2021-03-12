# https://atcoder.jp/contests/abc079/tasks/abc079_c

n = input()
# 入力値の桁数 - 1で数字の隙間の個数を取得
# ex)n = 111の時、隙間は「1■1■1」の2個なので2となる
op_cnt = len(n) - 1

# bit全探索する
for i in range(2 ** op_cnt):
    # あらかじめ ["-", "-", "-"] というリストを作っておく
    op = ["-"] * op_cnt

    # 隙間の数だけ検算する
    for j in range(op_cnt):
        # 右端から順に、1で論理積をとってtrueかどうか
        if((i >> j) & 1):
            # 条件を満たしていれば、フラグが立っていた場所を "+" で上書き
            # ex)i = 111 op_cnt = 2、j = 1のとき、
            # op[2 - 1 - 1] = op[0]
            # op[0] = "+" 
            op[op_cnt - 1 - j] = "+"

    formula = ""

    # nとopをzipでまとめ、それぞれp_nとp_oに入れる
    # ex)n = 122 op = ["+","-"]のとき、
    # 1ループ目:formula = 「1 +」
    # 2ループ目:formula = 「1 + 2 -」
    # 2ループ目:formula = 「1 + 2 - 2」
    for p_n,p_o in zip(n,op + [""]):
        formula += (p_n + p_o)

    # eval:引数の文字列を「文字列」ではなく「式」として評価する
    # ex)formula = "1 + 2 - 2"のとき、
    # eval(formula) = 1
    if eval(formula) == 7:
        print(formula + "=7")
        break
