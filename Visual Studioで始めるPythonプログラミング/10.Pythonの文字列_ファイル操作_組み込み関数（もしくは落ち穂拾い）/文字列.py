# ----------------------------------------------------------------------------------------
# 文字列
# ----------------------------------------------------------------------------------------

# 〇文字列はシングルクオート／ダブルクオート、あるいはこれらを3つ連続したもので囲む
# 〇Pythonでは文字列はUnicode文字が連続したもの（シーケンス）として扱われる
# 〇関数／クラス／モジュールでは「docstring」と呼ばれる特別な使い方がされる

# ダブルクオートとシングルクオートで囲んだ文字列
# シングルクォート内ではダブルクォートをエスケープせずに使用できるが、
# シングルクォートを使うには「\」でエスケープする必要がある。逆も同様。
s = 'It\'s beautiful "snake"!!!'
print(s) # It's beautiful "snake"!!!
s = "It's beautiful \"snake\"!!!"
print(s) # It's beautiful "snake"!!!

# エスケープ文字「\」をエスケープなしで使用するには、文字列を囲む最初の
# シングルクォート/ダブルクォートに「r」を付加する
# このような文字列を「raw string」と呼ぶ
path = r"c:\project\python"
print(path) # c:\project\python

# \tはタブ文字を示す
s = 'f\tbar'
print(s) # f       bar
# raw stringにするとただの文字列として認識されている
s = r'f\tbar'
print(s) # f\tbar

# 文字列に対して反復処理を行う
s = "python"
for c in s:
    print(c)
# p
# y
# t
# h
# o
# n

# トリプルクォート(三重引用符)は改行を含む文字列を記述する際に利用する
# 「'''」「"""」で囲まれるので、途中に単独の「'」「"」を自由に含めることができる
s = """It's snake that is
"good snake" for our friends!"""
print(s) # It's snake that is
         # "good snake" for our friends!

# 空白文字で区切られた文字列リテラルは単一の文字列リテラルになる
s = "poison" ".snake"
print(s) # poison.snake

# ----------------------------------------------------------------------------------------
# docstring
# ----------------------------------------------------------------------------------------

# pythonでは、docstringと呼ばれる文字列の使い方をすることで、
# 関数/クラス/モジュールにドキュメントを付加することがとても簡単に行えるようになっている
# 簡単に言うと、関数／クラス／モジュール定義の先頭の式がリテラル文字列の場合、
# それがそのドキュメントとして扱われる

def hello():
    # 関数helloの先頭の式がリテラル文字式となっているので、これはdocstringとして扱われる
    '''print "Hello world" だよ'''
    print('Hello world')

hello() # Hello world
help(hello) # Help on function hello in module 文字列:

# docstringは関数helloの属性「__doc__」として保存される
hello.__doc__ # hello()
              #     print "Hello world" だよ