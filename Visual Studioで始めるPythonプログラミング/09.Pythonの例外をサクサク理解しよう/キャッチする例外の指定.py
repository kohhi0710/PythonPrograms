# ----------------------------------------------------------------------------------------
# キャッチする例外の指定
# ----------------------------------------------------------------------------------------

# pythonでは、except節でキャッチする例外を個別に指定していき、
# 最後に「ワイルドカードのexcept節」を記述することが推奨されている
def func(exp):
    try:
        print(eval(exp))
    except ZeroDivisionError:
        print("division by zero")
    except NameError:
        print("undefined name")

func("1/0") # division by zero
func("undefinedvar + 2") # undefined name

# 「ワイルドカードのexcept節」がないので、異なる型同士の加算はキャッチされなかった
# func("1 + str(100)") # エラー
# ---------------------------------------------------------------
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 3, in func
#  File "<string>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ---------------------------------------------------------------

# Exceptionクラスを最初に指定している
# ZeroDivisionErrorとNameErrorはExceptionクラスの派生クラスなので、
# ZeroDivisionErrorとNameErrorのどちらが発生してもexcept Exceptionが実行されてしまう
def func(exp):
    try:
        print(eval(exp))
    except Exception:
        print("some exception!")
    except ZeroDivisionError:
        print("division by zero")
    except NameError:
        print("undifined name")

func("1/0") # some exception!
func("undefinedvar + 2") # some exception!

# 例外オブジェクトを取得する
for item in ["1 / 0","hoge + 2","1 + str(100)"]:
    try:
        print(eval(item))
    # 変数eに例外オブジェクトを取得している
    # 例外オブジェクトのメンバ「args」にはエラーメッセージが格納されている
    # 「e」だけでもエラーメッセージにアクセスできる
    except ZeroDivisionError as e:
        print("division by zero:",e)
    except NameError as e:
        print("undefined name:",e)
    except TypeError as e:
        print("incompatible types:",e,e.args)
# ↓実行結果
# devision by zero: division by zero
# undefined name: name 'hoge' is not defined
# incompatible types: unsupported operand type(s) for +: 'int' and 'str'
#    ("unsupported operand type(s) for +: 'int' and 'str'",)

# ----------------------------------------------------------------------------------------
# else節
# ----------------------------------------------------------------------------------------

# 関数funcにelse節とfinally節を追加
# 例外が何も発生しなければ、except節の代わりにelse節が実行される
def func(exp):
    try:
        print(eval(exp))
    except ZeroDivisionError:
        print("division by zero")
    except NameError:
        print("undefined name")
    except Exception:
        print("some excepton!")
    else:
        print("success!")
    finally:
        print("finally clause")

# 成功する場合
func("1 + 1")
# 2
# success!        # else節が実行された
# finally clause  # finally節が実行される

#失敗する場合
func("1 / 0")
# division by zero
# finally clause  # else節は実行されず、finally節が実行される