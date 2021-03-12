inputPath = 'C:/Folder/フィールド.csv'
input = open(inputPath,"r")
outputPath = 'C:/Folder/フィールド_SQLクエリ用.txt'
output = open(outputPath,'w')

count = 0
EndPoint = 145

inputlist = list(input.readline().split(","))

for item in inputlist:

    if count == EndPoint:
        print(output.write("Nz(ワークエクセルデータ." + item + ")"))
        break

    print(output.write("Nz(ワークエクセルデータ." + item + "),"))
    count += 1

input.close()
output.close()