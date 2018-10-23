#raw --> excel로 쓰기 (예 :  128*128의 셀에 데이터 쓰기)

import os
from xlsxwriter import Workbook
import math


infilename = 'D:\image\Axial_T2_512.raw'
outfilename = 'D:\image\Axial_T2_512.xlsx'

wb = Workbook(outfilename)
ws = wb.add_worksheet('Axial_T2_512')

with open(infilename,'rb') as fReader :
    fsize = os.path.getsize(infilename)
    XSIZE = YSIZE = int(math.sqrt(fsize))

# 워크시트에 열너비 지정
    ws.set_column(0,XSIZE,1.0)                          #약 0.34쯤
    for r in range(YSIZE):
        ws.set_row(r,9.5)                               #약 0.35쯤


    for rowNum in range(XSIZE):
        for colNum in range(YSIZE):
            data = int(ord(fReader.read(1)))
#data값으로 셀의 배경색을 조절 #000000~#FFFFFF(00=>0,ff=>255: r,g,b의 255값==>ffffff)
            if data>15:
                hexStr = '#'+(hex(data)[2:])*3
            else:
                hexStr = '#' + ('0'+hex(data)[2:]) * 3

            cell_format = wb.add_format()               #빈 셀 포맷
            cell_format.set_bg_color(hexStr)
            ws.write(rowNum,colNum,'',cell_format)


wb.close()
