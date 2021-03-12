# https://algoful.com/Archive/Algorithm/ShellSort

def shell_sort(array):
    n = len(array)
    h = 0

    # 3h + 1間隔
    while h <= n / 9 : h = 3 * h + 1
    while h > 0:

        # デバッグ用
        print("while h = ",h)

        # 間隔hで挿入ソート、最終的に挿入ソート
        for i in range(h,n):
            # 挿入する値を退避
            tmp = array[i]
            # 挿入する必要があるか
            if tmp < array[i - h]:
                # 挿入する位置
                j = i

                while True:
                    # hうしろにずらす
                    array[j] = array[j - h]
                    j -= h

                    if j < h or tmp >= array[j - h]:
                        break
                # 空いた位置に退避していた値を挿入
                array[j] = tmp

        h = int(h / 3)


list = list([9,4,0,4,9,6,3,2,0,3])
shell_sort(list)
print(list)
