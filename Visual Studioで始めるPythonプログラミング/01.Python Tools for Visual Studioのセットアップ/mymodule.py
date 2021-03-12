# --------------メインプログラムに書き込むコード例-----------
# import sys
# from mymodule import fact,fib

# print(sys.version)
# print("factorial of 3 is {0}".format(fact(3)))

# for n in range(7):
#     print("fib({0}) is {1}".format(n,fib(n)))
# -----------------------------------------------------------

# 階乗を返す関数 
# ex:3!(3 * 2 * 1)
def fact(n):
    # 引数が1以下の時、1を返す
    if(n <= 1):
        return 1

    # 再帰を利用し、nが0になるまで階乗を繰り返す

    # ex)n = 3のとき
    # 親:n = 3 return 3 * fact(3 - 1)
    # 子1:n = 2 return 2 * fact(2 - 1)
    # 子2:n = 1 return 1 * fact(1 - 1)
    # 子3:n = 0 return 1

    # 子3から遡って計算すると…

    # 子3:return 1
    # 子2:return 1 * 1 = 1
    # 子1:return 2 * 1 = 2
    # 親:return 3 * 2 = 6

    else:
        return n * fact(n -1)

# フィボナッチ数列を返す関数
def fib(n):
    if(n < 0):
        return -1
    elif(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        # ex)n = 5のとき
        # 親:n = 5 return fib(5 - 2) + fib(5 - 1)
        # 子1:retun fib(3 - 2) + fib(4 - 1)
        return fib(n - 2) + fib(n - 1)
