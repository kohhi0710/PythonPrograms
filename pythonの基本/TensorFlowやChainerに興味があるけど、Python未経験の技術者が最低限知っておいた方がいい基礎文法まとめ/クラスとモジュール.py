# ----------------------------------------------------------------------------------------
# クラス
# ----------------------------------------------------------------------------------------

# クラス変数はclassキーワードを記述した直下のブロックで定義する。
# インスタンス作成時にメンバを初期化するには、__init__メソッドを使用する。
# また、インスタンスメソッドはその呼び出し時に暗黙の第1引数としてインスタンス（self）が渡される。
# __init__メソッドやインスタンスメソッドではこれを利用して、インスタンス変数にアクセスを行う。

# @classmethodで修飾されたメソッドはクラスメソッドとなる。
# @staticmethodで修飾されたメソッドはスタティックメソッドとなる。
# 前者は呼び出し時に暗黙の第1引数としてクラスが渡されるが、
# 後者ではクラスに関する情報は渡されないのが、両者の大きな違いとなる。
# スタティックメソッドはクラスに関連するが、クラス情報やインスタンス情報を必要としない処理を
# 記述するのに使える。

class MyClass:
    clsvar = "class var"

    def __init__(self, foo = "foo",bar = "bar"):
        self.foo = foo
        self.bar = bar

    def instance_method(self):
        print(self.foo,self.bar)

    @classmethod
    def cls_method(cls):
        print(str(cls))

    @staticmethod
    def static_method():
        print("static method")

# クラス変数にはクラス経由でアクセスできる
print(MyClass.clsvar)

# クラスのインスタス作成(newは不要)
c = MyClass()

# インスタンスメソッド呼び出し
c.instance_method() # foo bar

# クラスメソッド呼び出し
MyClass.cls_method() # <class '__main__.MyClass'>

# スタティックメソッド呼び出し
MyClass.static_method() # static method

# ----------------------------------------------------------------------------------------
# モジュールのインポート
# ----------------------------------------------------------------------------------------

# randomモジュールのインポート
import random
# randomモジュールが公開している関数randintを呼び出す
print(random.randint(1,10)) # 7

# osモジュールが公開している関数getcwdをインポート
from os import getcwd
print(getcwd()) # C:\folder\hebi_project\hebi_project

# sysモジュールをsystemとしてインポート
import sys as system
print(system.version) # 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)]

# datetimeモジュールのdateクラスをDとしてインポート
from datetime import date as Date
d = Date(2016,10,31)
print(d) # 2016-10-31

# randomモジュールから関数randintと関数choiceをインポート
from random import randint,choice
print(choice(list(range(10)))) # 5

# 自作モジュールをインポート(同じフォルダにアルヨ)
import mylib

# mylibモジュールの関数sumを呼び出す
mylib.sum(100)