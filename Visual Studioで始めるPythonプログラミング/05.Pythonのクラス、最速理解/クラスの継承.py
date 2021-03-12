# ----------------------------------------------------------------------------------------
# クラスの継承
# ----------------------------------------------------------------------------------------

# pythonは、基底クラスを指定しない場合、クラスはobjectクラスの派生クラスとなる
# 基底クラスを指定してクラスを定義するには、次の「class 派生クラス名(基底クラス名のリスト):」
# のように基底クラスを指定する

# 基底クラスがBaseクラスであることを表している
class Base:
    def __init__(self, base_mem):
        self.base_mem = base_mem

class Derived(Base):
    # self:インスタンス自身を示すもの
    def __init__(self, base_mem,derived_mem):
        # super:基底クラスを参照する組み込み関数
        # 基底クラスBaseの__init__メソッドを参照している
        super().__init__(base_mem) # 基底クラスBaseの__init__にbase_memの値をセット
        self.derived_mem = derived_mem # 自クラスDerivedのderived_memに引き数のderived_memをセット

# Derivedクラスの__init__メソッドに引数をセット
d = Derived("base","derived")
print(d.base_mem) # base
print(d.derived_mem) # derived

# ----------------------------------------------------------------------------------------
# インスタンスメソッドのオーバーライド
# ----------------------------------------------------------------------------------------

class Base:
    def __init__(self, base_mem):
        self.base_mem = base_mem

    # 追加インスタンスメソッド
    def method(self):
        print("method on Base")

class Derived(Base):
    def __init__(self, base_mem,derived_mem):
        super().__init__(base_mem)
        self.derived_mem = derived_mem

    # 追加インスタンスメソッド
    def method(self):
        # 隠蔽されたメソッドを呼び出す時はsuper関数で基底クラスにアクセスする
        super().method()
        print("method on Derived")

d = Derived("base","derived")
# Derivedメソッドのmethodを呼び出す
# Baseクラスのmethodは名前が被り、隠蔽されている
d.method() # method on Derived