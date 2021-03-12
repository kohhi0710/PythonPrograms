# ----------------------------------------------------------------------------------------
# Pythonの例外
# ----------------------------------------------------------------------------------------

# インデントを間違えているのでエラーが発生する
# 構文解析時に発生する
# def func():
# print("hello")

# ゼロ除算エラー
if 1 / 0:
    print("oops")
# ---------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# ---------------------------------------

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

getsubcls(BaseException)
# BaseException
#   Exception
#     SystemError
#       CodecRegistryError
#     MemoryError
#     Error
#       … 省略 …
#     ArithmeticError
#       FloatingPointError
#       OverflowError
#       ZeroDivisionError ★
#     LookupError
#       … 省略 …
#     EOFError
#     NameError
#       … 省略 …
#     SyntaxError
#       IndentationError ★
#         TabError
#       … 省略 …
#     RuntimeError
#       RecursionError
#       NotImplementedError
#         … 省略 …
#   GeneratorExit
#   SystemExit
#   KeyboardInterrupt