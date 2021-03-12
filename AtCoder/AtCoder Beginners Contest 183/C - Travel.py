# https://atcoder.jp/contests/abc183/tasks/abc183_c

# sys:pythonのインタプリタや実行環境に関する情報を扱うためのライブラリ
# 使用しているプラットフォームを調べる時や、スクリプトの起動パラメータを取得する時に使う
# 標準ライブラリなので追加インストールは必要がない
# 参考:https://qiita.com/jp0003menegi/items/fbf407af7d294c09481a
import sys

# math:数学的な計算をするのに役立つ標準モジュール
# 参考:https://techacademy.jp/magazine/34137
import math

# itertools:イテレータ(配列やそれに類似する集合的データ構造の各要素に対する繰り返し処理の抽象化)ツール。
# 参考:https://qiita.com/anmint/items/37ca0ded5e1d360b51f3
import itertools as it

def IntParse():
    return int(sys.stdin.readline().replace("\n",""))

def IntParseSplit():
    return map(int,sys.stdin.readline().replace("\n","").split())

def StrParse():
    return str(sys.stdin.readline().replace("\n","").split())

def ListParse():
    return list(sys.stdin.readline().replace("\n",""))

def IntParseSplit_RoopRead():
    return [int(k) for k in sys.stdin.readline().replace("\n","").split()]

# lambda:無名関数。引数：戻り値で定義する。
def Lx(k):
    return list(map(lambda x : (int(x) * -k),sys.stdin.readline().replace("\n","").split()))

# 再帰の最大数を設定する
sys.setrecursionlimit(10 ** 6)

# おまじない　static void main(string[] args)
# このクラスがimportされた時は勝手に動かないようにする
if __name__ == "__main__":
    n,k = IntParseSplit()
    t = [IntParseSplit_RoopRead() for i in range(n)]

    # 距離d,前に訪れた都市last,巡回した都市のbit
    def f(d,last,bit):
        # bit全探索:「n個の選択肢それぞれにYes or Noの二択があるが、その部分集合(選択できるパターン)の
        # 全てを網羅的にチェックしたい」という場合に使えるアルゴリズム。
        # Yes or Noの二択がn箇所あるのでパターン数は2^n(何も選ばないという選択肢もパターンに含まれる)
        # この選択肢の1つ1つを2進数のbitに見立ててシフト演算でチェックを行うことから
        # 「bit全探索」とよばれるが、やってることは単なる全探索である。
        # 参考:https://qiita.com/gogotealove/items/11f9e83218926211083a

        # ex)n = 4のとき、(1 << 4) - 1
        # 00001を4ビットシフト → 10000 - 00001 → 01111(15と0の全16パターン)
        if bit == (1 << n) - 1:
            # d(距離)に訪れた都市の移動距離を入力
            # ex)入力値「0 1 10 100」のとき、t[0][0] = 0
            # dに0を加算
            # 2ループ目は1になるのでdに1を加算 
            d += t[last][0]

            # 移動距離dが指定の距離kと同じかどうか?
            if d == k:
                return 1
            else:
                return 0

        cnt = 0

        # 都市の数だけループ
        for i in range(1,n):
            # bit検算
            # 1をiビットシフトした値とbitの論理積をとる
            if bit & (1 << i):
                # trueの場合、次のループへ
                continue
            # fの再帰処理
            # (距離累積 + 訪れた都市の距離、都市ナンバー、巡回した都市のbit)
            cnt += f(d + t[last][i],i,bit | 1 << i)

        return cnt

    print(f(0,0,1))

