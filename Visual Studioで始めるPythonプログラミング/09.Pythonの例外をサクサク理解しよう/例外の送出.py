# ----------------------------------------------------------------------------------------
# 例外の送出
# ----------------------------------------------------------------------------------------

# raise:任意の例外を任意の時点で送出できる
# raise RuntimeError
# --------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# RuntimeError
# --------------------------------------

# コンストラクタにエラーメッセージを引き渡すこともできる
# raise RuntimeError("hello from runtime error")
# --------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# RuntimeError: hello from runtime error
# --------------------------------------

# 例外処理時に、その例外を適切に処理できなかったときは単に「raise」とするだけで
# 例外を送出することができる。
def func(exp):
    try:
        return eval(exp)
    except ZeroDivisionError:
        print("division by zero")
        raise
    except NameError as e:
        print("undefined name")
        raise
    # 発生した例外(Exception)からさらに例外(RuntimeError)を発生させている
    # このとき、新たに発生した例外の原因を「from」に続けて記述する
    except Exception as e:
        print("some exception!",e)
        raise RuntimeError(e.args) from e

def caller():
    x = input("input expression:")
    print(func(x))

# 例外の再送出
caller() # inputで「1/0」を入力する
# ↓実行結果
# division by zero
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "C:\Work\_kohira\C# test\ppppp\hebi_project\hebi_project\VisualStudio\Visual Studioで始めるPythonプログラミング\9.Pythonの例外をサクサク理解しよう\例外の送出.py", line 40, in caller
#     print(func(x))
#   File "C:\Work\_kohira\C# test\ppppp\hebi_project\hebi_project\VisualStudio\Visual Studioで始めるPythonプログラミング\9.Pythonの例外をサクサク理解しよう\例外の送出.py", line 25, in func
#     return eval(exp)
#   File "<string>", line 1, in <module>
# ZeroDivisionError: division by zero

# 例外の連鎖
caller() # inputで「1 + str(100)」を入力する
# ↓実行結果
# Traceback (most recent call last):
#   File "C:\Work\_kohira\C# test\ppppp\hebi_project\hebi_project\VisualStudio\Visual Studioで始めるPythonプログラミング\9.Pythonの例外をサクサク理解しよう\例外の送出.py", line 25, in func
#     return eval(exp)
#   File "<string>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 
# The above exception was the direct cause of the following exception:
# 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "C:\Work\_kohira\C# test\ppppp\hebi_project\hebi_project\VisualStudio\Visual Studioで始めるPythonプログラミング\9.Pythonの例外をサクサク理解しよう\例外の送出.py", line 40, in caller
#     print(func(x))
#   File "C:\Work\_kohira\C# test\ppppp\hebi_project\hebi_project\VisualStudio\Visual Studioで始めるPythonプログラミング\9.Pythonの例外をサクサク理解しよう\例外の送出.py", line 36, in func
#     raise RuntimeError(e.args) from e
# RuntimeError: ("unsupported operand type(s) for +: 'int' and 'str'",)

# 最初の例（「1/0」）では、exceptionsample.pyファイルの3行目（「eval(exp)」行）で
# 発生した例外がそのまま再送出されている。

# 2つ目の例では、同様に3行目で発生したTypeError例外を直接の原因としてRuntimeError例外が
# 送出されたことが分かる（スタックトレースが2つあり、その後者の
# 「raise RuntimeError(e.args) from e」でRuntimeError例外が送出されたことが分かる）。

# ----------------------------------------------------------------------------------------
# 独自の例外クラスの作成
# ----------------------------------------------------------------------------------------

# Exceptionクラスやその派生クラスを独自クラスの基底クラスとすることがポイント
# pythonではユーザー定義の例外クラスはExceptionクラスの派生クラスであることが必要になるので注意
class MyException(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyException("hello")
except MyException as e:
    print(e)