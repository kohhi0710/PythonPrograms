# https://algoful.com/Archive/Algorithm/InsertionSort

def insertion_sort(array):
    n = len(array)

    for i in range(1,n):
        # 挿入する値を退避
        tmp = array[i]

        # 挿入する必要があるか
        if tmp < array[i - 1]:
            # 挿入する位置
            j = i

            while True:
                # 1つ後ろにずらす
                array[j] = array[j - 1]
                j -= 1

                if j == 0 or tmp >= array[j - 1]:
                    break

            # 空いた位置に退避していた値を挿入
            array[j] = tmp


list = list([9,4,0,4,9,6,3,2,0,3])
insertion_sort(list)
print(list)
