# 拡張モジュールNumpyをインポート
# 計算がすごく早くなるすごいモジュールらしい
import numpy as np

N = int(input())
# 入力を取り込む
# [::-1]でリストを逆順にする　必ず先にnp.sortしなければならない(reverseが存在していないため)
# forで取得した配列を格納した変数iの型をintに変換し、np.arrayに入れている
a_n = np.sort(np.array([int(i) for i in input().split()]))[::-1]

# Aliceの値は0スタート2ステップで値を取り出し合計
# Bobの値は1スタート2ステップで値を取り出し合計
# Aliceの値からBobの値を引いて出力
print(sum(a_n[::2]) - sum(a_n[1::2]))
