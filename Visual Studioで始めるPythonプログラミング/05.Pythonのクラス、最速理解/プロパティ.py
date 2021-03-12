# ----------------------------------------------------------------------------------------
# プロパティ
# ----------------------------------------------------------------------------------------

# ゲッターとセッターを定義したプロパティクラス
class Baz:
    def __init__(self, name):
        self._name = name

    # getter
    def getname(self):
        return self._name

    # setter
    def setname(self,value):
        self._name = value

    # property:引数は(fget = None, fset = None, fdel = None, doc = None)
    # fget = プロパティを取得するメソッド
    # fset = プロパティを設定するメソッド
    # fdel = プロパティを削除するメソッド
    # fdoc = プロパティの説明文
    # setter(fset)を設定しなければ読み取り専用プロパティとなる
    name = property(getname,setname)

# インスタンスの生成
b = Baz("hogehoge")
# getterにとぶ
print(b.name) # hogehoge
b.name = "hogeeeeeeeeen"
print(b.name) # hogeeeeeeeeen

# @propertyデコレータを使用してBuzクラスを書き直したもの
# pythonには「プライベート」という概念がなく、全てのメンバが基本的には外部に公開される

class Buz:
    def __init__(self, name):
        self._name = name

    # getterとなるメソッドに「@property」をつけてメソッド名をプロパティ名にする
    @property
    def name(self):
        return self._name

    # setterとなるメソッドには「@プロパティ名.setter」と修飾する。
    # メソッド名はプロパティ名と同じものにする
    @name.setter
    def name(self,value):
        self._name = value

class Baz:
    def __init__(self,name,addr):
        self._name = name
        self.addr = addr

    # name.setter修飾されたメソッドがないので、
    # nameは読み取り専用プロパティ
    @property
    def name(self):
        return self._name

b = Baz("三田","兵庫県")
b.addr = "Kobe"
# 変数bが参照するオブジェクトにインスタンス変数を追加
b.prop = "フラワータウン"
print(b.addr)
# メソッドも追加できる
b.method = lambda x:print("b.method:",x)
b.method("hoge")
# b.name = "nameプロパティは読み取り専用なのでエラーがでますよ"








