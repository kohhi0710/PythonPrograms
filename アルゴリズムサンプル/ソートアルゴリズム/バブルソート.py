# https://algoful.com/Archive/Algorithm/BubbleSort#sample-cs

def bubble_sort(array):
    # 配列の長さ
    n = len(array)

    # 配列分ループ
    # iに先頭要素の値を代入
    for i in range(n - 1):
        # jに末尾要素の値を代入、iの値(先頭要素)までデクリメントループ
        for j in range(n - 1,i, -1):
            # jよりiのほうが大きければswap
            if array[j] < array[j - 1]:
                # tmpに末尾要素を退避
                tmp = array[j]
                # j(末尾)にi(先頭要素)を入れる
                array[j] = array[j - 1]
                # 退避しておいたjの値をiに入れる→位置が交換される
                array[j - 1] = tmp
                print(array) # デバッグ用

list = list([9,4,0,4,9,6,3,2,0,3])
bubble_sort(list)
print(list)
