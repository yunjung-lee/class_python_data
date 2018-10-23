# Excel 파일 처리 1
import xlrd

input_file = 'd:/pydata/csv/sales_2013.xlsx'

workbook = xlrd.open_workbook(input_file)

sheetCount = workbook.nsheets # 속성

for  worksheet  in workbook.sheets() :
    sheetName = worksheet.name
    sRow = worksheet.nrows
    sCol = worksheet.ncols
    print(sheetName, sRow, sCol)