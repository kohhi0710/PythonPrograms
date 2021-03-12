# ----------------------------------------------------------------------------------------
# パッケージ
# ----------------------------------------------------------------------------------------

# 複数のモジュールで構成される、より大規模な再利用可能コード群
# pythonでは多くの場合、何らかのディレクトリ以下に含まれるサブディレクトリおよびモジュールによって構成される

# パッケージとモジュールのインポート
import mypackage

print(mypackage) # <module 'mypackage' from 'C:\\ディレクトリ\\mypackage\\__init__.py'>

# print(mypackage.mymodule1) # エラーになる。
# トップレベルのパッケージをインポートしたからといって、
# その下のモジュールが自動的にインポートされるわけではない
# -----------------------------------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: module 'mypackage' has no attribute 'mymodule1'
# -----------------------------------------------------------------

# パッケージに含まれるモジュールをインポートする方法
# 〇形式1
import mypackage.mymodule1
# 〇形式2
from mypackage import mymodule1

print(mypackage.mymodule1.foo()) # hello from foo on mypackage.mymodule1

# dir関数を使って現在のローカルスコープに導入されている名前を調べることができる
import mypackage.mymodule1
print(dir()) # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'mypackage']
print(dir(mypackage)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'mymodule1']

# 形式2でモジュールをインポートして現在のローカルスコープを参照
from mypackage import mymodule1
print(dir()) # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'mymodule1']
print(dir(mymodule1)) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'foo']

# 関数fooのインポート
from mypackage.mymodule1 import foo
foo() # hello from foo on mypackage.mymodule1
