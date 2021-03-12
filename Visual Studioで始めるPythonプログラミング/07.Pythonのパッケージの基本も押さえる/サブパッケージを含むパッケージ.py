# ----------------------------------------------------------------------------------------
# サブパッケージを含むパッケージ
# ----------------------------------------------------------------------------------------

# パッケージがサブパッケージを含んでいる場合は、以下のようにしてサブパッケージのインポートが可能
import mypackage.subpackage.submodule1
print(mypackage.subpackage.submodule1.bar()) # hello from bar on subpackage.submodule1

from mypackage.subpackage import submodule2
print(submodule2.bar()) # hello from bar on subpackage.submodule2

# 「from mypackage import *」ではサブパッケージの内容はインポートされない
from mypackage import *
print(dir()) # ['__builtins__', '__doc__', '__loader__', '__name__', 
             #  '__package__', '__spec__', 'mymodule1', 'mymodule2']

# subpackageを明示的にインポートすることで、サブパッケージのモジュールがローカルスコープに加わる
from mypackage.subpackage import *
print(dir()) # ['__builtins__', '__doc__', '__loader__', '__name__', 
             #  '__package__', '__spec__', 'submodule1', 'submodule2']
