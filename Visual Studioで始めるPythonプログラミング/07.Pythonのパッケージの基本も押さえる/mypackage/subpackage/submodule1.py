# パッケージ内のモジュールから、同一パッケージ内の別モジュールを参照する
# 同じsubpackage内のsubmodule2の関数barをbazという名前でインポートしている
from mypackage.subpackage.submodule2 import bar as baz

# 「.」を利用してい階層をさかのぼる相対的な方法(相対インポート)でも指定できる
# この場合、「.」は現在のパッケージ、「..」は親パッケージに相当する
from .submodule2 import bar as baz

# 親階層「..」によりmypackage階層を参照し、そこからさらに階層を下っている
from ..mymodule import foo
from ..subpackage.submodule2 import bar as baz

# 詳しい説明 https://qiita.com/ysk24ok/items/2711295d83218c699276

print("hello from subpackage.submodule1")

def bar():
    print("hello from bar on subpackage.submodule1")
