# ----------------------------------------------------------------------------------------
# 文字列
# ----------------------------------------------------------------------------------------

# シングルクォートで囲んだ文字列
s1 = 'snake\'s eye.'
# シングルクォートをエスケープ
s1 = 'snake\'s eye. ' "hello"
# ダブルクォートで囲んだ文字列
s2 = "snake's eye. \"hello\""
print(s1) # snake's eye. "hello"
print(s2) # snake's eye. "hello"

# トリプルクォートは入力内容がそのまま文字列となる
s3 = '''snake's eye.  
"hello"''' # snake's eye. "hello"
s4 = """snake's eye.
"hello\""""
print(s3) # snake's eye.
          # "hello"
print(s4) # snake's eye.
          # "hello"

# 数値の文字列化
s = str(1)
print(s) # 1
print(type(s)) # <class 'str'>

# リストの文字列化
s = str([1,2,3])
print(s) # [1, 2, 3]
# 先頭の3文字を出力
print(s[0:3]) # [1,

# ----------------------------------------------------------------------------------------
# 文字列操作メソッド
# ----------------------------------------------------------------------------------------

# s.capitalize():
# 文字列の先頭を大文字化、残りを小文字化

# s.center(width[,fillchar]):
# 文字列をセンタリング

# s.count(sub[,start[,end]]):
# start～end内でのsubの発生回数を取得

# s.endswith(suffix[,start[,end]]):
# start～endで指定された範囲がsuffixで終了するか

# s.startswith(plefix[,start[,end]]):
# 同様に範囲内でplefixで始まるか

# s.expandtabs(tabsize = 8):
# 文字列内のタブ文字を空白文字に展開(tabsize引数の省略時は8タブとみなされる)

# s.find(sub[,start[,end]]):
# start～end内でsubを検索し、見つかればそのインデックス位置を、見つからなければ-1を返す

# s.index(sub[, start[, end]]):
# start～end内でsubを探索(見つからないと例外が発生)

# s.format(*args,**kwargs):
# 文字列の書式化

# s.isalnum():
# 文字列が英数字で構成されているか

# s.isalpha():
# 文字列が英字で構成されているか

# s.isdecimal():
# 文字列が10進数字で構成されているか

# s.isdigit():
# 文字列が10進数字で構成されているか

# s.isnumeric():
# 文字列が数を表す文字で構成されているか

# s.islower():
# 全て小文字か

# s.isupper():
# 全て大文字か

# s.isprintable():
# 印字可能文字か

# s.isspace():
# 空白文字か

# s.istitle():
# 文字列がタイトルケースか

# s.title():
# 文字列をタイトルケース化(先頭の文字を大文字化)

# s.join(iterable):
# iterableの要素を変数sの内容で区切って連結

# s.lower():
# 小文字化

# s.upper():
# 大文字化

# s.replace(old,new[,count]):
# 文字列中のoldをnewでcount回(省略時は全て)置き換えた文字列を返送

# s.rstrip(char):
# 文字列末からcharで指定した文字を削除(省略時は空白文字を削除)

# s.lstrip(char):
# 文字列先頭からcharで指定した文字を削除(省略時は空白文字を削除)

# s.split(sep, maxsplit = -1):
# sepを区切り文字としてmaxsplit回文字列を分割したリストを返送する
# （maxsplit引数を省略した場合は分割が全て行われる）

# s.rsplit(sep, maxsplit = 1):
# sepを区切り文字として文字列末尾から分割をしていく
# （maxsplit引数を省略した場合は分割が全て行われる）

# -----------------
# 文字列操作の例
# -----------------

#タブ展開
print('a\tb'.expandtabs()) # a       b

# 文字列検索
print('snake.net'.find('ake')) # 2
print('snake.net'.index('.net')) # 5
print('snake.net'.endswith('net')) # True
print('snake.net'.startswith('sna')) # True

# 文字列の書式化
print('{0} + {1} = {2}'.format(1,2,1 + 2)) # 1 + 2 = 3

# 文字列が〇〇か
print('foo'.isalnum()) # True
print('a1'.isalpha()) # False
print('abc'.isalpha()) # True
print('123'.isdecimal()) # True
print('123'.isdigit()) # True
print('123'.isnumeric()) # True
print('ABC'.islower()) # False
print('abc'.islower()) # True
print('ABC'.isupper()) # True
print('abc'.isupper()) # True
print('a'.isprintable()) # True
print('\t'.isprintable()) # False
print('\n'.isspace()) # True
print(' '.isspace()) # True
print('snake.net'.istitle()) # False

# 丸付き数字の1は数字か(①)
# isdecimalではFalse
print(chr(0x2460).isdecimal()) # False
# isdigitではTrue
print(chr(0x2460).isdigit()) # True
# isnumericでもTrue
print(chr(0x2460).isnumeric()) # True

# 「1/7」は数字か(⅐)
# isdecimalではFalse
print(chr(0x2150).isdecimal()) # False
# isdigitでもFalse
print(chr(0x2150).isdigit()) # False
# isnumericではTrue
print(chr(0x2150).isnumeric()) # True

# 文字列を改変(した新しい文字列を取得)
print('BAR'.capitalize()) # Bar
print('foo'.center(7,'*')) # **foo**
print('foo'.count('o')) # 2
print('snake.net'.title()) # Snake.Net
print('.'.join(['snake','net'])) # snake.net
print(','.join([str(x) for x in range(3)])) # 0,1,2
print('AbC'.lower()) # abc
print('AbC'.upper()) # ABC
print('snake.net'.replace('snake','hebi')) # hebi.net
print('snakesnakesnake'.replace('snake','hebi',2)) # hebihebisnake
print('snake '.rstrip()) # snake
print('snake2'.rstrip("2")) # snake
print(' foo'.lstrip()) # foo
print('1 2 3 4 5'.split()) # ['1', '2', '3', '4', '5']
print('1 2 3 4 5'.split(' ',2)) # ['1', '2', '3 4 5']
print('1 2 3 4 5'.rsplit(' ',2)) # ['1 2 3', '4', '5']