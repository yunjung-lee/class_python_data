# (1) 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리)
#
# (2) 텍스트마이닝 기반 데이터 분석 (부제: 텍스트 기반 데이터 분석 및 처리)
#
# (3) 빅데이터 분석 결과 시각화 (부제 : 데이터베이스 기반 데이터 분석 및 GUI 시각화)
#
#
# 복습퀴즈1. 엑셀파일을 읽어서 마지막 시트를 화면에 출력한다.
#
# 복습퀴즈2. 엑셀파일을 읽어서 모든 시트를 화면에 출력한다. 단,
#
#       제목행은 제일 위에 한번만 출력한다.
#
#
# 복습퀴즈3(선택) 폴더를 선택한 후, 그 폴더의 모든 엑셀파일을 목록으로 보여준다.
#
#    그리고 선택한 엑셀파일의 모든 시트 목록을 보여준다. 마지막을 선택한
#
#    시트를 화면에 출력한다.

from tkinter import *

from tkinter.simpledialog import *

from tkinter.filedialog import *

import csv

import json

import os

import os.path

import xlrd

import xlwt


#함수부
def drawSheet(cList):
    global csvList, cellList, input_file

    if cellList == None or cellList == []:
        pass
    else:
        for row in cellList:
            for col in row:
                col.destroy()

    rowNum =  len(cList)
    colNum = len(cList[0])
    cellList = []

    for row in range(rowNum):
        tmpList =[]
        for col in range(colNum):
            ent = Entry(window,text ='')
            tmpList.append(ent)
            ent.grid(row = row, column = col)
        cellList.append(tmpList)

    for i in range(0,rowNum):
        for k in range(0,colNum):
            cellList[i][k].insert(0,cList[i][k])


def openCSV():
    global csvList, cellList, input_file
    csvList = []

    input_file = askopenfilename(parent = window, filetype = (("CSV파일","*.csv"),("모든 파일","*.*")))

    filereader =  open(input_file,'r', newline="")

    header  = filereader.readline()
    header = header.strip()
    print(header)
    header_list = header.split(',')

    csvList.append(header_list)

    for row in filereader:
        row = row.strip()
        for i in csv.reader([row], skipinitialspace = True):
            csvList.append(i)

    drawSheet(csvList)
    filereader.close()

def openJSON():
    global csvList, cellList, input_file
    csvList = []

    input_file = askopenfilename(parent = window, filetype = (("JSON파일","*.json"),("모든 파일","*.*")))

    filereader =  open(input_file,'r', newline="",encoding="utf-8")

    jsonDic = json.load(filereader)
    csvName = list(jsonDic.keys())
    jsonList = jsonDic[csvName[0]]

    header_list = list(jsonList[0].keys())
    csvList.append(header_list)

    for tmpDic in jsonList:
        tmpList = []
        for header in header_list:
            data = tmpDic[header]
            tmpList.append(data)
        csvList.append(tmpList)

    drawSheet(csvList)

    filereader.close()

def openExcel01():
    global csvList, cellList, input_file
    csvList = []

    input_file = askopenfilename(parent = window, filetype = (("Excel파일","*.xlx;*.xlsx"),("모든 파일","*.*")))

    workbook = xlrd.open_workbook(input_file)

    sheet1 = workbook.sheets()[-1]
    sheetName =sheet1.name
    sRow = sheet1.nrows
    sCol = sheet1.ncols
    for i in range(sRow):
        tmpList = []
        for k in range(sCol):
            value = sheet1.cell_value(i,k)
            tmpList.append(value)
        csvList.append(tmpList)

    drawSheet(csvList)

def openExcel02():
    global csvList, cellList, input_file
    csvList = []

    input_file = askopenfilename(parent=window, filetype=(("Excel파일", "*.xlx;*.xlsx"), ("모든 파일", "*.*")))

    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets

    for workSheet in workbook.sheets():
        sheetName = workSheet.name
        sRow = workSheet.nrows
        sCol = workSheet.ncols

def saveCSV():
    global csvList, cellList, input_file
    pass

def saveJSON():
    global csvList, cellList, input_file
    pass

def saveExcel():
    global csvList, cellList, input_file
    pass




#변수부
csvList, cellList = [],[]
input_file = ''


#메인코드부

window = Tk()


mainMenu = Menu(window)
window.configure(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = 'CSV열기', command = openCSV)
fileMenu.add_command(label = 'JSON열기', command = openJSON)
fileMenu.add_command(label = 'Excel 마지막 시트 열기', command = openExcel01)
fileMenu.add_command(label = 'Excel 선택 열기', command = openExcel02)
fileMenu.add_separator()
fileMenu.add_command(label = 'CSV저장', command = saveCSV)
fileMenu.add_command(label = 'JSON저장', command = saveJSON)
fileMenu.add_command(label = 'Excel저장', command = saveExcel)



window.mainloop()


































































































