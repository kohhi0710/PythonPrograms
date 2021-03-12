# ----------------------------------------------------------------------------------------
# 辞書
# ----------------------------------------------------------------------------------------

# 直接的な辞書の作成
d = {'key':'value','foo':'bar'}
print(d) # {'key': 'value', 'foo': 'bar'}

# 組み込み関数dictにキーと値を指定して作成
d = dict(foo = 'foo',bar = 'bar')
print(d) # {'foo': 'foo', 'bar': 'bar'}

# 内包表記による作成
d = {chr(x + ord('a')): x + ord('a') for x in range(5)}
print(d) # {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}
l = [tuple((chr(x + ord('a')),x + ord('a'))) for x in range(5)]
print(l) # [('a', 97), ('b', 98), ('c', 99), ('d', 100), ('e', 101)]

# リストから辞書を作成
d = dict(l)
print(d) # {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}

# len(d):
# 辞書dの項目数を取得

# d[key]:
# keyに対応する値を取得。keyがなければkeyError例外が発生する

# d[key] = new value:
# keyに対応する値を変更する

# del d[key]:
# キーに対応する値を削除

# k in d , k not in d:
# 辞書dでのキーkの有無を確認

# d.clear():
# 辞書dの全要素を削除

# d.copy():
# 浅いコピーを作成

# d.get(key[,default]):
# 辞書dからkeyに対応する値を取得。keyがなければdefaultの値が返される(デフォルト値はNone)

# d.items():
# 辞書dからキー/値を要素とするビューオブジェクトを作成(forループなどで使用)

# d.keys():
# 辞書dからキー要素とするビューオブジェクトを作成

# d.pop(key[,default]):
# 指定したkeyの値を辞書dから削除

# d.values():
# 辞書dから値を要素とするビューオブジェクトを作成

# d.update(other):
# 辞書dをotherで更新

# --------------
# 辞書の操作例
# --------------

print(d) # {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}
print(d['a']) # 97

# d[key]形式ではkeyが存在しないとKeyErrorが発生する
# print(d['z']) # エラー
# --------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'z'
# --------------------------------------

# d.get(key)ではkeyが存在しないと(デフォルトで)Noneが戻る
print(d.get('Z')) # None
print(d.get('a')) # 97
print('c' in d) # True

# 辞書のキー/値の組に対して反復処理
for k,v in d.items():
    print(k,v) # a 97
               # b 98
               # c 99
               # d 100
               # e 101

# 辞書のキーに対して反復処理
for k in d.keys():
    print(k,d[k]) # a 97
                  # b 98
                  # c 99
                  # d 100
                  # e 101

# 辞書に要素を追加
d['f'] = 102
print(d) # {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102}
# 辞書から要素を削除
del d['f']
print(d) # {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101}

# 2要素のタプルを要素とする別のリスト
l2 = [tuple((chr(x + ord('a')),x + ord('a'))) for x in range(5,10)]
print(l2) # [('f', 102), ('g', 103), ('h', 104), ('i', 105), ('j', 106)]
# そのリストを基に辞書を更新
d.update(l2)
print(d) # {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106}
# キーを指定して辞書を更新
d.update(k = 107)
print(d) # {'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107}

# ----------------------------------------------------------------------------------------
# 集合
# ----------------------------------------------------------------------------------------

# 要素の重複を許さず、また順序性を持たないデータ構造。
# ある値が集合に存在するかを確認したり、集合演算を行ったりする際に使用できる。
# 要素変更可能な集合set型と、不可能な集合frozenset型がある。

# 直接的な集合の作成
s = {'a','b','c'}
print(s) # {'a','b','c'}

# 内包表記による作成
s = {chr(x + ord('a')) for x in range(5)}
print(s) # {'a', 'e', 'b', 'c', 'd'}
l = list(range(5))
print(l) # [0, 1, 2, 3, 4]

# リストをもとに組み込み関数setを使って集合を作成
s = set(l)
print(s) # {0, 1, 2, 3, 4}

# 変更不可能な集合の作成
frset = frozenset(s)
print(frset) # frozenset({0, 1, 2, 3, 4})

# len(s):
# 集合の要素数を求める

# x in s , x not in s:
# 集合sに要素xが含まれているか

# s1.isdisjoint(s2):
# 集合s1と集合s2は互いに素か

# s1.issubset(s2) , s1 <= s2:
# 集合s1が集合s2の部分集合か

# s1 < s2:
# 集合s1が集合s2の真部分集合か(s2がs1のすべての要素に加えて別の要素を持つか)

# s1.issuperset(s2) , s1 >= s2:
# 集合s1が集合s2の上位集合か(s1がs2を包含しているか)

# s1 > s2:
# 集合s1と集合s2の真上位集合か(s1がs2のすべての要素に加えて別の要素を持つか)

# s1.union(s2) , s1 | s2:
# 集合s1と集合s2の和

# s1.intersection(s2) , s1 & s2:
# 集合s1と集合s2の積

# s1.difference(s2) , s1 - s2:
# 集合s1と集合s2の差

# s1.symmetric_difference(s2) , s1 ^ s2:
# 集合s1と集合s2の対称差(いずれかにのみ含まれる要素)

# s.copy():
# 集合sの浅いコピーを作成

# ----------------
# 集合の操作の例
# ----------------

s1 = set(range(5))
s2 = set(range(5,10))
s3 = set(range(10))
print(s1) # {0, 1, 2, 3, 4}
print(s2) # {5, 6, 7, 8, 9}
print(s3) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

print(s1.issubset(s3)) # True
print(s1.isdisjoint(s2)) # True

# s1と同じ要素からなる別の集合
s4 = set(range(5))
print(s4) # {0, 1, 2, 3, 4}

# s1はs4の部分集合だが、真部分集合ではない
print(s1 <= s4) # True
print(s1 < s4) # False

# s1はs4の上位集合ｄが、真上位集合ではない
print(s1 >= s4) # True
print(s1 > s4) # False

print(s1.union(s2)) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.intersection(s3)) # {0, 1, 2, 3, 4}
print(s3.difference(s1)) # {8, 9, 5, 6, 7}

s5 = set(range(6))

print(s1.symmetric_difference(s5)) # {5}

# --------------------------------------
# set型(変更可能な集合)でのみ使える操作
# --------------------------------------

# s1.add(x):
# 集合sに要素xを追加

# s.remove():
# 集合sから要素xを排除(なければKeyError発生)

# s.discard(x):
# 集合sに要素xがあれば削除(なくても例外は発生しない)

# s.pop():
# 集合sから任意の要素を取り出して削除

# s.clear():
# 集合sの全要素を削除

# s1.update(s2) , s1 |= s2:
# 集合s1に集合s2を追加

# s1.intersection_update(s2) , s1 &= s2:
# 集合s1の要素をs1とs2の積とする

# s1.difference_update(s2) , s1 -= s2:
# 集合s1の要素を集合s2との差にする

# s1.symmetric_difference_update(s2) , s1 ^= s2:
# 集合s1の要素を集合s2との対称差にする

# --------------------------------
# 変更可能な集合に対する操作の例
# --------------------------------

print(s1) # {0, 1, 2, 3, 4}

# s1に要素「5」を追加
s1.add(5)
print(s1) # {0, 1, 2, 3, 4, 5}

# removeメソッドは要素がないとKeyErrorを発生する
# s1.remove(6) # エラー
# -------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 6
# -------------------------------------

# discardメソッドは要素がなくてもKeyErrorとならない
s1.discard(6)

print(s2) # {5, 6, 7, 8, 9}

# s1の要素をs1とs2の和にする
s1 |= s2
print(s1) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}