# https://algoful.com/Archive/Algorithm/SelectionSort

def selection_sort(array):
    n = len(array)

    for i in range(0,n-1):
        min = i
        for j in range(i + 1,n):
            if array[min] > array[j]:
                min = j

            else:
                tmp = array[min]
                array[min] = array[i]
                array[i] = tmp

list = list([9,4,0,4,9,6,3,2,0,3])
selection_sort(list)
print(list)
