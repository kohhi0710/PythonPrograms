# 関数を定義
def funcSumOdDigits(val):
    # 引数を文字列型に変換
    tmp1 = str(val)
    # listを宣言し、mapでintに変換したあと代入
    tmp2 = list(map(int,tmp1))
    # listの値を合計し、tmpsumに代入
    tmpsum = sum(tmp2)
    # 戻り値
    return tmpsum

# 変数を3つ宣言し、標準入力の値をsplitでばらしてそれぞれに入れる
N,A,B = map(int,input().split())
ans = 0

# ループ
# range関数の引数を２つ設定すると、第一引数と第二引数の連番が生成される。
# ex)N = 20であれば1から19まで生成される(1が20回足される)
# ex)20自体も含めたいならN + 1とする
for i in range(1,N + 1):
    sumOfDigits = funcSumOdDigits(i)

    # sumOfDigitsの値がA以上かつB以下の場合
    if A <= sumOfDigits and sumOfDigits <= B:
        # ansをiの値分増加させる
        ans += i 

print(ans)