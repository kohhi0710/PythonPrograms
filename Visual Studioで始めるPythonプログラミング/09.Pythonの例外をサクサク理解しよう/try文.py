# ----------------------------------------------------------------------------------------
# try文
# ----------------------------------------------------------------------------------------

# try文の基本形
# ----------------------------------------------------------
try:
    # 例外が発生する可能性のあるコード
    pass
except:
    # 例外発生時に実行するコード
    pass
finally:
    # 例外の有無にかかわらず最後に実行されるコード
    pass
# ----------------------------------------------------------

# あるクラスの派生クラスを一覧表示する関数
def getsubcls(cls,n = 0):
    # 最初だけ特別にインデントなしでクラス名を表示
    if n == 0:
        print(cls.__name__)

    # 指定されたクラスの派生クラスを反復する
    for subcls in cls.__subclasses__():
        # インデント付きでクラス名表示
        print('  ' * (n+1), subcls.__name__, sep='')
        # そのクラスが派生クラスを持っていればそれらを表示
        getsubcls(subcls, n + 1)

# 存在していないクラスを関数に渡してみる
# →NameError例外が発生する
# getsubcls(SomeException)
# ----------------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'SomeException' is not defined
# ----------------------------------------------

# try文を使用して例外処理をする
try:
    getsubcls(SomeException)
except:
    print("定義されたクラス名を指定してください")
finally:
    print("tryブロックの最終節です")

# 既存の例外クラスである「ArithmeticError」クラスを渡して例外を発生させないtry文を書く
# →except節は実行されず、Finally節は実行する
try:
    getsubcls(ArithmeticError)
except:
    print("定義されたクラス名を指定してください")
finally:
    print("tryブロックの最終節です")
