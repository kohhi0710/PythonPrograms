# ----------------------------------------------------------------------------------------
# __init__.pyファイルのall変数
# ----------------------------------------------------------------------------------------

# emailパッケージ内のすべてのモジュールをインポート
from email import *
print(dir()) # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
             #  '__package__', '__spec__', 'base64mime', 'charset', 'encoders', 'errors', 
             #  'feedparser', 'generator', 'header', 'iterators', 'message', 
             #  'message_from_binary_file', 'message_from_bytes', 'message_from_file', 
             #  'message_from_string', 'mime', 'parser', 'quoprimime', 'utils']

# 同じように自作パッケージでモジュールを全インポートしてみると…
from mypackage import *

# mypackageが表示されていない
print(dir()) # ['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

# mypackageという名前は定義されていないので、エラーになる
# print(mypackage)
# ----------------------------------------------
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'mypackage' is not defined
# ----------------------------------------------

# Pythonのチュートリアルドキュメントによると…
# 「パッケージの __init__.py コードに __all__ という名前のリストが定義されていれば、 
# from package import * が現れたときに import すべきモジュール名のリストとして使う」
# 「もしも __all__ が定義されていなければ、実行文 from sound.effects import * は、
# パッケージ sound.effects の全てのサブモジュールを現在の名前空間の中へ import しません」

# 要するに、
# 「from パッケージ import *」を実行したときに、パッケージ中のどのモジュールをインポートさせるかは
# パッケージの作者が明示的に指定をしなければならず、
# そのためには__init__.pyファイルの中で__all__変数にインポートするものを指定する必要がある」
# ということである。

# __init__.pyに「mymodule1」を定義後、インポートを実施する
# 「mymodule2」の定義ができていない場合は、全インポートでもmymodule2はインポートされない
from mypackage import *
print(dir()) # ['__builtins__', '__doc__', '__loader__', '__name__', 
             #  '__package__', '__spec__', 'mymodule1']

# 定義後、インポートすると反映される
from mypackage import mymodule2
print(dir()) # ['__builtins__', '__doc__', '__loader__', '__name__', 
             #  '__package__', '__spec__', 'mymodule2']
mymodule2.foo() # this is mypackage.mymodule2.foo speaking