# ----------------------------------------------------------------------------------------
# グローバル変数「__name__」
# ----------------------------------------------------------------------------------------

# グローバル変数「__name__」は、モジュールがインポートされた場合にはそのモジュール名が、
# そうではなく「〇〇.py」のように実行された場合には「__main__」という値が設定される
# この値を調べることで、モジュールがpythonのスクリプトファイルとして実行されているのか、
# 対話ウィンドウやその他のpythonスクリプトでモジュールがインポートされているのかを判断できる

print(__name__)

def hello(name):
    print("hello",name)

def goodbye(name):
    print("goodbye",name)

# このモジュールをpythonスクリプトとして実行すると、printが実行される。
# importされると、変数__name__の値ががモジュール名「その他の重要なこと」になるので、ifの分岐内に入れない
if __name__ == "__main__":
    print("hello from python");

# ----------------------------------------------------------------------------------------
# コマンドライン引数
# ----------------------------------------------------------------------------------------

# sys.argv:コマンドライン引数を格納するリスト
from sys import argv

# argv[0]には実行されるモジュールの名前が格納される
if __name__ == "__main__":
    print(argv) # ex:['その他の重要なこと.py', 'arg1', 'arg2']

print("hello from python module")

# ----------------------------------------------------------------------------------------
# 引数が整数値なら加算、そうでなければ文字列として連結
# ----------------------------------------------------------------------------------------

# 関数add内でreモジュールのfullmatch関数を使い、渡された2つの値がどちらも整数として扱えるか判定
# trueなら和を、Falthなら文字列として連結する

from sys import argv
# reモジュールからfullmatch関数をインポート
from re import fullmatch

def add(arg1,arg2):
    if fullmatch("[-+]{0,1}\d+",str(arg1)) and fullmatch("[-+]{0,1}\d+",str(arg2)):
        return "sum: " + str(int(arg1) + int(arg2))
    else:
        return "concatnate: " + str(arg1) + str(arg2)

# スクリプトとして呼び出された際はコマンドライン引数の数を調べて、
# 数が足らなければ使い方を示すメッセージを表示し、
# そうでなければコマンドライン引数を渡して関数addを呼び出す
if __name__ == "__main__":
    if len(argv) < 3:
        print("usage : python その他の重要なこと.py arg1 arg2")
    else:
        print(add(argv[1],argv[2]))