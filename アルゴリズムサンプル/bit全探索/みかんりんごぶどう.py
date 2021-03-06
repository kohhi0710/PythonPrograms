# 参考:https://qiita.com/gogotealove/items/11f9e83218926211083a

# -例題- 
# みかん（100円）りんご（200円）ぶどう（300円）が
# それぞれ1つずつ果物屋さんにありました。
# 財布の中には300円ありますが、
# 考え得るすべての買い物パターンを列挙しなさい。

# -考え方-
# 全ての買い物パターンで合計金額を計算し、
# その中から300円以下で済んだものを列挙する

# 2~3 = 8パターンの中から300円以下のものを列挙する

money = 300
item = (("みかん",100),("りんご",200),("ぶどう",300))

n = len(item)

# 各アイテムを買うor買わないを
# 「2進数のそれぞれの桁が0であるのか1であるのか(左からみかん、りんご、ぶどう)」
# で表現すると、以下のような表になる。

# -10進数表記-　-2進数表記-　-買い物リスト-
# 0        　   000        　何も買わない
# 1        　   001       　 ぶどう
# 2        　   010      　　りんご
# 3        　   011     　   りんご+ぶどう
# 4        　   100     　   みかん
# 5        　   101     　   みかん+ぶどう
# 6        　   110     　　 みかん+りんご
# 7        　   111    　　  みかん+りんご+ぶどう

# 全パターンループ
for i in range(2 ** n):
    bag = []
    total = 0

    # アイテムの個数分ループ
    for j in range(n):
        # 順に右にシフトさせ、最下位bitのチェックを行う
        # 下から0桁目が1であればぶどう入り
        # 下から1桁目が1であればりんご入り
        # 下から2桁目が1であればみかん入り

        #2進数の一番右からチェックを開始していく

        # ex)i = 6、j = 0の場合(ぶどうチェック)
        # 6の2進数「110」を0ビット右シフトすると「110」
        # 最下位の値を1で論理和をとるとfalseになるので「ぶどう無し」

        # ex)i = 6、j = 1の場合(りんごチェック)
        # 6の2進数「110」を1ビット右シフトすると「011」
        # 最下位の値を1で論理和をとるとtrueになるので「りんご入り」

        # ex)i = 6、j = 2の場合(みかんチェック)
        # 6の2進数「110」を2ビット右シフトすると「001」
        # 最下位の値を1で論理和をとるとtrueになるので「みかん入り」
        if((i >> j) & 1):
            # フラグが立っていたら、bagに果物をつめる
            # [j](itemの要素番号) [0](果物名)
            bag.append(item[j][0])
            # 買い物累計額にも加算
            # [1](果物金額)
            total += item[j][1]

    # totalが300以下の時、合計金額と配列bagに格納されている果物名を出力
    if(total <= money):
        print(total,bag)

def test():
    # 2進数表記した場合の下から数えてｎ桁目(一番下の桁を0とする)が
    # 1であるかどうかをチェックするコードは「(i >> n) & 1」である。
    # これは、「iをn回右にシフトして1(2進数001)と論理積をとる(最下位の桁が1であるかどうかチェックする」
    # ということになる。
    
    i = 5

    # 5を2進数で表記すると101
    bin(i) 
    # 5を2回右にシフトすると001
    bin(i >> 2)
    # 5を2回右にシフトしたものと
    # 1の論理積は1(=True)
    print((i >> 2) & 1)
