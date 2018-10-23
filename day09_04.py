from  tkinter import *

from  tkinter.simpledialog import *

from  tkinter.filedialog import *

import csv

import json

import  os

import os.path
import xlrd
import xlwt
import sqlite3


def drawSheet(cList) :

    global cellList



    if cellList == None or cellList == [] :



        pass

    else :



        for row in cellList:

            for col in row:

                col.destroy()




    rowNum = len(cList)

    colNum = len(cList[0])

    cellList = []

    # 빈 시트 만들기

    for i in range(0, rowNum):

        tmpList = []

        for k in range(0, colNum):

            ent = Entry(window, text='')

            tmpList.append(ent)

            ent.grid(row=i, column=k)

        cellList.append(tmpList)

    # 시트에 리스트값 채우기. (= 각 엔트리에 값 넣기)

    for i in range(0, rowNum):

        for k in range(0, colNum):

            cellList[i][k].insert(0, cList[i][k])






def openCSV() :

    global  csvList, input_file

    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))

    filereader = open(input_file, 'r', newline='')

    header = filereader.readline()

    header = header.strip()  # 앞뒤 공백제거

    header_list = header.split(',')

    csvList.append(header_list)

    for row in filereader:  # 모든행은 row에 넣고 돌리기.

        row = row.strip()

        for i in csv.reader([row],skipinitialspace=True):
            csvList.append(i)




    drawSheet(csvList)




    filereader.close()




def openJSON() :

    global  csvList, input_file

    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("JSON파일", "*.json"), ("모든파일", "*.*")))

    filereader = open(input_file, 'r', newline='', encoding='utf-8')




    jsonDic = json.load(filereader)

    csvName = list(jsonDic.keys())

    jsonList = jsonDic[csvName[0]]

    # 헤더 추출

    header_list = list(jsonList[0].keys())

    csvList.append(header_list)

    # 행들 추출

    for tmpDic in jsonList:

        tmpList = []

        for header in header_list:

            data = tmpDic[header]

            tmpList.append(data)

        csvList.append(tmpList)




    drawSheet(csvList)




    filereader.close()




def  saveCSV() :

    global csvList, input_file

    if csvList == [] :

        return

    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv',

               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))

    filewriter = open(saveFp.name, 'w', newline='')

    for  row_list  in  csvList :

        row_str = ','.join(map(str, row_list))

        filewriter.writelines(row_str + '\n')




    filewriter.close()




def  saveJSON() :

    global csvList, input_file

    if csvList == [] :

        return

    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.json',

               filetypes=(("JSON파일", "*.json"), ("모든파일", "*.*")))

    filewriter = open(saveFp.name, 'w', newline='')

    # csvList --> jsonDic

    fname = os.path.basename(input_file).split(".")[0]

    jsonDic = {}

    jsonList = []

    tmpDic = {}

    header_list = csvList[0]

    for i in range(1, len(csvList)) :

        rowList = csvList[i]

        tmpDic = {}

        for k in range(0, len(rowList)) :

            tmpDic[header_list[k]] = rowList[k]

        jsonList.append(tmpDic)




    jsonDic[fname] = jsonList

    json.dump(jsonDic, filewriter, indent=4)

    filewriter.close()



def  saveExcel() :
    global csvList, input_file

    if csvList == []:
        return

    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.xls',

                           filetypes=(("Excel파일", "*.xls"), ("모든파일", "*.*")))
    fileName = saveFp.name

    outWorkbook = xlwt.Workbook()                                                              #Workbook :  excel file
    outSheet = outWorkbook.add_sheet('sheet1')                                          #이름을 추후에 지정

    for i in range (len(csvList)):
        for k in range(len(csvList[i])):
            outSheet.write(i,k,csvList[i][k])

    outWorkbook.save(fileName)


def csvData01() :

    global  csvList

    csvList = []

    input_file = "d:\\pydata\\csv\\supplier_data.csv"

    filereader = open(input_file, 'r', newline='')

    header = filereader.readline()

    header = header.strip()  # 앞뒤 공백제거

    header_list = header.split(',')

    # part Number, Purchase Date

    idx1 = 0

    for h in header_list:

        if h.strip().upper() == 'part Number'.strip().upper():

            break

        idx1 += 1

    idx2 = 0

    for h in header_list:

        if h.strip().upper() == 'Purchase Date'.strip().upper():

            break

        idx2 += 1

    if idx1 > idx2:

        idx1, idx2 = idx2, idx1

    del (header_list[idx2])

    del (header_list[idx1])

    csvList.append(header_list)

    for row in filereader:  # 모든행은 row에 넣고 돌리기.

        row = row.strip()

        row_list = row.split(',')

        del (row_list[idx2])

        del (row_list[idx1])

        if row_list[0] == 'Supplier Y':

            continue

        cost = float(row_list[2][1:])

        cost *= 1.5

        cost = int(cost / 100) * 100

        cost_str = "${0:.2f}".format(cost)

        row_list[2] = cost_str

        csvList.append(row_list)




    drawSheet(csvList)

    filereader.close()




def csvData02() :

    global csvList

    csvList = []

    input_file = "d:/pyData/csv/supplier_data.csv"

    filereader = open(input_file, 'r', newline='')

    csvReader = csv.reader(filereader) # CSV 전용으로 열기

    header_list = next(csvReader)

    csvList.append(header_list)

    for row_list in csvReader:  # 모든행은 row에 넣고 돌리기.

        csvList.append(row_list)




    drawSheet(csvList)

    filereader.close()




def csvData03() :  # 여러개 csv 파일의 행개수 합계 궁금함.

    global csvList

    csvList = []

    dirName = askdirectory()

    # 폴더에서 *.csv 파일 목록만 뽑기

    import glob

    import os

    file_list = glob.glob(os.path.join(dirName, "*.csv"))

    for  input_file  in  file_list :

        filereader = open(input_file, 'r', newline='')

        csvReader = csv.reader(filereader)  # CSV 전용으로 열기

        header_list = next(csvReader)

        rowCount = 0

        for  row in csvReader :

            rowCount += 1

        csvList.append([os.path.basename(input_file),'-->', rowCount])

        filereader.close()




    drawSheet(csvList)

def excelData01():
    global  csvList, input_file

    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("CSV파일", "*.xlx;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets  # 속성

    for worksheet in workbook.sheets():
        sheetName = worksheet.name
        sRow = worksheet.nrows
        sCol = worksheet.ncols
        print(sheetName, sRow, sCol)


def excelData02():
    global  csvList, input_file

    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("CSV파일", "*.xlx;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets  # 속성
    sheet1 = workbook.sheets()[0]
    sheetName = sheet1.name
    sRow = sheet1.nrows
    sCol =sheet1.ncols
    # print(sheetName, sRow, sCol)
    for i in range(sRow):
        tmpList = []
        for k in range(sCol):
            value = sheet1.cell_value(i,k)
            tmpList.append(value)
        csvList.append(tmpList)

    drawSheet(csvList)


def excelData03():
    global  csvList, input_file

    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("CSV파일", "*.xlx;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets  # 속성
    # sheet1 = workbook.sheets()[0]
    # sheet2 = workbook.sheets()[1]
    # sheet3 = workbook.sheets()[2]
    for sh in workbook.sheets():
        # sheetName = sh.name
        sRow = sh.nrows
        sCol =sh.ncols
        # print(sheetName, sRow, sCol)
        for i in range(sRow):
            tmpList = []
            for k in range(sCol):
                value = sh.cell_value(i,k)
                tmpList.append(value)
            csvList.append(tmpList)

    drawSheet(csvList)

def excelData04():
    global  csvList, input_file

    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("CSV파일", "*.xlx;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets  # 속성
    sheetNum = 0
    for worksheet in workbook.sheets():
        sheetNum +=1
        sheetName = worksheet.name
        sRow = worksheet.nrows
        sCol = worksheet.ncols
        print(sheetNum, sheetName)

    num = 0
    num = input('sheet 번호 : ')

    sheet1 = workbook.sheets()[int(num)-1]
    sheetName = sheet1.name
    sRow = sheet1.nrows
    sCol =sheet1.ncols
    # print(sheetName, sRow, sCol)
    for i in range(sRow):
        tmpList = []
        for k in range(sCol):
            value = sheet1.cell_value(i,k)
            tmpList.append(value)
        csvList.append(tmpList)

    drawSheet(csvList)

def excelData05():
    global  csvList, input_file

    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("CSV파일", "*.xlx;*.xlsx"), ("모든파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets  # 속성
    sheetNameList = []
    for worksheet in workbook.sheets():
        sheetNameList.append(worksheet.name)
##################subwindow###############################################################
    def selectSheet():
        selectedIndex = listbox.curselection()[0]          #기본은 하나지만 여러개도 리턴한다.(튜플)==>()[0] :  [0]을 표시해준다.
        subwindow.destroy()
        sheet1 = workbook.sheets()[selectedIndex]
        sRow = sheet1.nrows
        sCol = sheet1.ncols
        # print(sheetName, sRow, sCol)
        for i in range(sRow):
            tmpList = []
            for k in range(sCol):
                value = sheet1.cell_value(i, k)
                tmpList.append(value)
            csvList.append(tmpList)

        drawSheet(csvList)

    subwindow = Toplevel(window)                        #window의 하위 윈도우 생성
    listbox = Listbox(subwindow)
    button  = Button(subwindow,text = '선택', command = selectSheet)
    listbox.pack()
    button.pack()
    for sName in sheetNameList:
        listbox.insert(END,sName)
    subwindow.lift()

############################################################################################

def sqliteData01():

    con = sqlite3.connect('c:/temp/userDB')
    cur = con.cursor()

    #데이터베이스 내의 테이블 목록이 궁금
    # 특별한 테이블 sqlite_mater를 호출
    sql = "select name from sqlite_master where type = 'table'"
    cur.execute(sql)
    tableNameList = []
    while True :
        row = cur.fetchone()  # 하나씩 가져오는 명령어 모두 가져오면(fetchall) 메모리가 넘쳐서 안됨
        if row == None:
            break
        tableNameList.append(row[0])
    print(tableNameList)
    ##############subwindow###############################################################
    def selectTable():
        selectedIndex = listbox.curselection()[0]  # 기본은 하나지만 여러개도 리턴한다.(튜플)==>()[0] :  [0]을 표시해준다.
        subwindow.destroy()
        # #테이블의 열 목록 뽑기
        # sql = "select * from " + tableNameList[selectedIndex]
        # colNameList = []
        # for col in cur.description :
        #     colNameList.append(col[0])
        # print(colNameList)
        # colNameList = ["userID", "userName", "userAge"]
        sql = "select * from " + tableNameList[selectedIndex]
        cur.execute(sql)
        while True:
            row = cur.fetchone()
            if row == None:
                break
            row_list = []
            for ii in range(len(row)):
                row_list.append((row[ii]))
            csvList.append(row_list)
        drawSheet(csvList)                          #csvList 끝난 후 이므로 같은 열은 안됨


        cur.close()
        con.close()

        print('ok2')



    subwindow = Toplevel(window)  # window의 하위 윈도우 생성
    listbox = Listbox(subwindow)
    button = Button(subwindow, text='선택', command=selectTable)
    listbox.pack()
    button.pack()
    for sName in tableNameList:
        listbox.insert(END, sName)
    subwindow.lift()

    #####################################


    # sql = "select userID, userName, userAge from userTable"
    # cur.execute(sql)
    #
    #
    # header_list = ["userID", "userName", "userAge"]
    # csvList.append(header_list)
    #
    # while True:
    #         row = cur.fetchone()
    #         if row == None:
    #             break
    #         userID = row[0]
    #         userName = row[1]
    #         userAge = row[2]
    #         rowList = [userID, userName, userAge]
    #         csvList.append(rowList)
    #
    # drawSheet(csvList)





def sqliteData02():
    global csvList, input_file
    con = sqlite3.connect('c:/temp/userDB')
    cur = con.cursor()

#열이름 리스트 만들기
    colList = []
    for data in csvList[0]:
        colList.append(data.replace(' ',''))

    tableName = os.path.basename(input_file).split(".")[0]

#sql문을 만들때 띄어쓰기를 조심해야함 : 오류의 대부분임
    try:
        sql = "create table " + tableName +"("
        for colName in colList:
            sql += colName+" char(20),"
        sql = sql[:-1]
        sql+=")"
        cur.execute(sql)  # sql문을 커서로 날려라
        print(sql)
    except:
        pass

    for i in range(1,len(csvList)):
        rowList = csvList[i]
        sql = "insert into " + tableName+" values("
        for row in rowList:
            sql += "'" + row + "',"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)
        print(sql)

    con.commit()



    cur.close()
    con.close()

    print('ok')





## 전역 변수 ##

csvList, cellList = [], []

input_file = ''




## 메인 코드 ##

window = Tk()
window.geometry('600x800')



mainMenu = Menu(window)

window.config(menu=mainMenu)




fileMenu = Menu(mainMenu)

mainMenu.add_cascade(label='파일', menu=fileMenu)

fileMenu.add_command(label='CSV 열기', command=openCSV)

fileMenu.add_command(label='CSV 저장', command=saveCSV)

fileMenu.add_separator()

fileMenu.add_command(label='JSON 열기', command=openJSON)

fileMenu.add_command(label='JSON 저장', command=saveJSON)

fileMenu.add_separator()

fileMenu.add_command(label='Excel 저장', command=saveExcel)



csvMenu = Menu(mainMenu)

mainMenu.add_cascade(label='CSV 데이터 분석', menu=csvMenu)

csvMenu.add_command(label='특정 열,행 제거', command=csvData01)

csvMenu.add_command(label='csv 패키지 활용', command=csvData02)

csvMenu.add_command(label='여러 CSV 행수 알기', command=csvData03)


excelMenu = Menu(mainMenu)
mainMenu.add_cascade(label = 'Excel 데이터 분석',menu = excelMenu)
excelMenu.add_command(label = "Excel 정보 보기", command = excelData01)
excelMenu.add_command(label = "Excel 내용 보기 - 1st", command = excelData02)
excelMenu.add_command(label = "Excel 내용 보기 -All", command = excelData03)
# excelMenu.add_command(label = "Excel 내용 보기 -시트 선택", command = excelData04)            pycham창에서 입력받음
excelMenu.add_command(label = "Excel 내용 보기 -select", command = excelData05)

sqliteMenu = Menu(mainMenu)
mainMenu.add_cascade(label = 'SQLite 데이터 분석', menu = sqliteMenu )
sqliteMenu.add_command(label = 'SQLite정보 보기', command = sqliteData01)
sqliteMenu.add_command(label = 'SQLite정보 쓰기', command = sqliteData02)
window.mainloop()