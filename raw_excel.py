# RAW --> Excel 로 쓰기  (예 : 128x128의 셀에 데이터 쓰기)

from xlsxwriter import Workbook

import os

import math




inFileName = 'D:\images\Pet_RAW\Pet_RAW(64x64)\dog06_64.raw'

outFileName = 'D:\images\dog06_64#2.xlsx'




wb = Workbook(outFileName)

ws = wb.add_worksheet('dog06_64')




with open(inFileName, 'rb')  as  fReader :

    fsize = os.path.getsize(inFileName)

    XSIZE = YSIZE = int(math.sqrt(fsize))

    # 워크시트의 열 너비/ 행 높이를 지정..

    ws.set_column(0, XSIZE, 1.0)  # 약 0.34 쯤

    for  r  in range(YSIZE) :

        ws.set_row(r, 9.5)  # 약 0.35 쯤




    for  rowNum in range(XSIZE) :

        for colNum in range(YSIZE) :

            data = int(ord(fReader.read(1)))

            # data 값으로 셀의 배경색을 조절 #000000~#FFFFFF

            if data > 15 :

                hexStr = '#' + (hex(data)[2:])*3

            else :

                hexStr = '#' + ('0' + hex(data)[2:]) * 3




            # 셀의 포맷을 준비

            cell_format = wb.add_format()

            cell_format.set_bg_color(hexStr)




            ws.write(rowNum, colNum, '', cell_format)




wb.close()


