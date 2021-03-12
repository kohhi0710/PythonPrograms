# xlsxを加工してcsvにする

import xlrd
import pprint

wb = xlrd.open_workbook('C:/Folder/test.xlsx')
sheet = wb.sheet_by_name('Sheet1')

count = 0
EndPoint = 145

CSVPath = 'C:/Folder/test.csv'
f = open(CSVPath,'w')

while True:
    cell = sheet.cell(0, count)
    if count == EndPoint:
        print(f.write(cell.value))
        break

    print(f.write(cell.value + ","))
    count += 1

f.close()