# フィールド名一覧.txtを加工してcsvにする

textPath = ''C:/Folder/フィールド名一覧.txt'
input = open(textPath,"r")
CSVPath = 'C:/Folder/フィールド名一覧.csv'
output = open(CSVPath,'w')

count = 0
EndPoint = 145

while True:
    if count == EndPoint:
        print(output.write(input.readline()))
        break

    print(output.write(input.readline() + ","))
    count += 1

input.close()
output.close()