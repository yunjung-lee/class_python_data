from  tkinter import *
from  tkinter.simpledialog import *
from  tkinter.filedialog import *
import csv
import json
import glob
import os
import os.path
import xlrd
import xlwt
import sqlite3
import pymysql


## 전역 변수 ##
csvList, cellList = [], []
sheetName = None

## 함 수 ##

def drawSheet(cList) :
    global csvList, cellList

    if cellList==None or cellList ==[]:
        pass
    else:
        for row in cellList:
            for col in row:
                col.destroy()

    rowNum = len(cList)
    colNum = len(cList[0])
    cellList = []

    for i in range(rowNum):
        tmpList = []
        for k in range(colNum):
            ent = Entry(window, text = '')
            tmpList.append(ent)
            ent.grid(row=i,column=k)
        cellList.append(tmpList)

    for i in range(rowNum):
        for k in range(colNum):
            cellList[i][k].insert(0,cList[i][k])

    print('ok-1')

def openCSV():
    global csvList, cellList,input_file
    csvList = []

    input_file = askopenfilename(parent = window, filetypes = (("CSV파일", "*.csv"), ("모든 파일","*.*")))
    filereader = open(input_file, 'r', newline='')
    # csv패키지 없을 때 사용
    # header = filereader.readline()
    csvReader = csv.reader(filereader)
    header_list = next(csvReader)
    #csv패키지 없을 때 사용
    # header = header.strip()
    # header_list = header.split(",")
    csvList.append(header_list)

    for row_list in csvReader:
        # csv패키지 없을 때 사용
        # row = row.strip()
        # for row in csv.reader([row], skipinitialspace=True):
        #     row_list = row
        csvList.append(row_list)

    drawSheet(csvList)

    filereader.close()


def openJSON():
    global csvList, cellList,input_file
    csvList = []

    input_file = askopenfilename(parent = window, filetypes = (("JSON파일", "*.json"), ("모든 파일","*.*")))
    filereader = open(input_file, 'r', newline='',encoding="utf-8")

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


def openExcel():
    global csvList, cellList,sheetName,input_file
    csvList = []

    input_file = askopenfilename(parent=window, filetypes=(("엑셀파일", "*.xls;*.xlsx"), ("모든 파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    sheet1 = workbook.sheets()[0]
    sheetName = sheet1.name
    sRow = sheet1.nrows
    sCol = sheet1.ncols


    for i in range(sRow):
        tmpList = []
        for k in range(sCol):
            value = sheet1.cell_value(i,k)
            tmpList.append(value)
        csvList.append(tmpList)

    drawSheet(csvList)



def saveCSV():
    global csvList, cellList,input_file

    if csvList == []:
        return
    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv',filetypes=(("CSV파일", "*.csv"), ("모든 파일", "*.*")))
    filewriter = open(saveFp.name, 'w', newline='')

    csvWrite = csv.writer(filewriter)
    print(csvList)
    for row_list in csvList:
        csvWrite.writerow(row_list)

    filewriter.close()



def saveJSON():
    global csvList, cellList,input_file

    if csvList ==[]:
        return
    saveFp = asksaveasfile(parent = window, mode='w', defaultextension = '.json', filetypes = (("JSON파일","*.json"),("모든 파일","*.*")) )
    filewriter = open(saveFp.name, 'w', newline='')

    fname = os.path.basename(input_file).split(".")[0]

    jsonDic, tmpDic={},{}
    jsonList = []

    header_list = csvList[0]
    for i in range(1,len(csvList)):
        rowList =  csvList[i]
        tmpDic = {}
        for k in range(0,len(rowList)):
            tmpDic[header_list[k]] = rowList[k]
        jsonList.append(tmpDic)

    jsonDic[fname] = jsonList
    json.dump(jsonDic, filewriter, indent=4)

    filewriter.close()



def saveExcel():
    global csvList, cellList,input_file,sheetName

    if csvList ==[]:
        return
    saveFp = asksaveasfile(parent = window, mode='w', defaultextension = '.xls', filetypes = (("Excel파일","*.xls"),("모든 파일","*.*")) )
    fileName = saveFp.name

    outWorkbook = xlwt.Workbook()
    if sheetName == None or sheetName == '':
        outSheet = outWorkbook.add_sheet("sheet1")
    else:
        outSheet = outWorkbook.add_sheet(sheetName)

    for i in range(len(csvList)):
        for k in range(len(csvList[i])):
            outSheet.write(i,k,csvList[i][k])

    outWorkbook.save(fileName)



def csvData01():
    global csvList, cellList,input_file
    if csvList == [] :
        return

    idx1 = 0
    rowStr = askstring(str,"지우고 싶은 열이름:")
    for row in csvList[0]:
        print(row)
        if row == rowStr:
            break
        idx1 += 1

    del csvList[0][idx1]
    drawSheet(csvList)




def csvData02():
    global csvList, cellList,input_file
    if csvList == [] :
        return

    idx1 = 0
    colStr = askstring(str, "지우고 싶은 행 첫 data : ")
    for row in csvList[0]:
        print(row)
        if row == colStr:
            break
        idx1 += 1

    del csvList[idx1]
    drawSheet(csvList)



def csvData03():
    global csvList, cellList,input_file

    csvList = []
    dirName = askdirectory()

    file_list = glob.glob(os.path.join(dirName,'*.csv'))
    for input_file in file_list:
        filereader = open(input_file, 'r', newline='')
        csvReader = csv.reader(filereader)
        rowCount = 0
        for row in csvReader:
            rowCount +=1
        csvList.append([os.path.basename(input_file),'=>',rowCount])

        filereader.close()

    drawSheet(csvList)

def excelData01():
    global csvList, cellList, sheetName, input_file
    csvList = []

    input_file = askopenfilename(parent=window, filetypes=(("엑셀파일", "*.xls;*.xlsx"), ("모든 파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets
    sheet1 = workbook.sheets()[0]


    for worksheet in workbook.sheets():
        sheetName = worksheet.name
        sRow = sheet1.nrows
        sCol = sheet1.ncols
        print(sheetName,sRow,sCol)

    subWindow = Toplevel(window) # 부모(window)에 종속된 서브윈도
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text='sheet 이름 -->' + sheetName)
    label1.pack()
    label2 = Label(subWindow, text='열의 수 -->' + str(sCol))
    label2.pack()
    label3 = Label(subWindow, text='행의 수 -->' + str(sRow))
    label3.pack()
    subWindow.mainloop()



def excelData02():
    global csvList, cellList, sheetName, input_file
    csvList = []

    input_file = askopenfilename(parent=window, filetypes=(("엑셀파일", "*.xls;*.xlsx"), ("모든 파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetCount = workbook.nsheets

    for worksheet in workbook.sheets():
        sRow = worksheet.nrows
        sCol = worksheet.ncols

        for i in range(sRow):
            tmpList = []
            for k in range(sCol):
                value = worksheet.cell_value(i, k)
                tmpList.append(value)
            csvList.append(tmpList)
    drawSheet(csvList)




def excelData03():
    global csvList, cellList, input_file
    csvList = []

    input_file = askopenfilename(parent=window, filetypes=(("엑셀파일", "*.xls;*.xlsx"), ("모든 파일", "*.*")))
    workbook = xlrd.open_workbook(input_file)
    sheetNameList = []

    for worksheet in workbook.sheets():
        sheetNameList.append(worksheet.name)

    def selectSheet():
        selectedIndex = listbox.curselection()[0]
        subWindow.destroy()
        sheet1 = workbook.sheets()[selectedIndex]
        sRow = sheet1.nrows
        sCol = sheet1.ncols

        for i in range(sRow):
            tmpList = []
            for k in range(sCol):
                value = sheet1.cell_value(i,k)
                tmpList.append(value)
            csvList.append(tmpList)
        drawSheet(csvList)

    subWindow = Toplevel(window)
    listbox = Listbox(subWindow)
    button = Button(subWindow, text ="선택", command = selectSheet)

    listbox.pack()
    button.pack()

    for sName in sheetNameList:
        listbox.insert(END,sName)

    subWindow.lift()

def sqliteData01():
    con = sqlite3.connect('c:/temp/userDB')
    cur = con.cursor()

    sql = "SELECT name FROM sqlite_master WHERE type='table'"
    cur.execute(sql)

    tableNameList = []
    while True:
        row = cur.fetchone()
        if row == None:
            break

        tableNameList.append(row[0])


    ##################################
    def selectTable():
        selectedIndex = listbox.curselection()[0]
        subWindow.destroy()
        sql = "SELECT * FROM " + tableNameList[selectedIndex]
        cur.execute(sql)

        while True:
            row = cur.fetchone()
            if row == None:
                break

            row_list = []
            for ii in range(len(row)):
                row_list.append(row[ii])
            csvList.append(row_list)
            drawSheet(csvList)

        cur.close()

        con.close()  # 데이터베이스 연결 종료

        print('Ok!')



    subWindow = Toplevel(window)

    listbox = Listbox(subWindow)

    button = Button(subWindow, text='선택', command=selectTable)

    listbox.pack()
    button.pack()




    for sName in tableNameList:
        listbox.insert(END, sName)

    subWindow.lift()




def sqliteData02():
    global csvList, input_file

    con = sqlite3.connect('c:/temp/userDB')
    cur = con.cursor()

    colList = []

    for data in csvList[0]:
        colList.append(data.replace(' ', ''))
    tableName = os.path.basename(input_file).split(".")[0]

    try:
        sql = "CREATE TABLE " + tableName + "("
        for colName in colList:
            sql += colName + " CHAR(20),"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)

    except:
        pass

    for i in range(1, len(csvList)):
        rowList = csvList[i]
        sql = "INSERT INTO " + tableName + " VALUES("
        for row in rowList:
            sql += "'" + row + "',"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)

    con.commit()
    cur.close()
    con.close()

    print('Ok!')

def mysqlData01() :

    con = pymysql.connect(host='192.168.98.131', user='root', password='1234', db='userDB', charset='utf8')
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    csvList = []


    sql = "SHOW TABLES"
    cur.execute(sql)

    tableNameList = []
    while True :
        row = cur.fetchone()
        if row == None:
            break

        tableNameList.append(row[0]);




    ##################################

    def selectTable() :
        selectedIndex = listbox.curselection()[0]
        subWindow.destroy()

        colNameList = []
        sql = "DESC " + tableNameList[selectedIndex]
        cur.execute(sql)

        while True:
            row = cur.fetchone()
            if row == None:
                break

            colNameList.append(row[0]);




        csvList.append(colNameList)
        sql = "SELECT * FROM " + tableNameList[selectedIndex]
        cur.execute(sql)

        while True:
            row = cur.fetchone()
            if row == None:
                break

            row_list = []
            for ii in range(len(row)) :
                row_list.append(row[ii])
            csvList.append(row_list)

            drawSheet(csvList)

    subWindow = Toplevel(window)
    listbox = Listbox(subWindow)
    button = Button(subWindow, text='선택', command=selectTable)
    listbox.pack(); button.pack()

    for  sName in tableNameList :
        listbox.insert(END, sName)
    subWindow.lift()




def mysqlData02() :
    global csvList, input_file

    con = pymysql.connect(host='192.168.174.129', user='root', password='1234', db='userDB', charset='utf8')
    cur = con.cursor()

    colList = []
    for data in csvList[0] :
        colList.append(data.replace(' ', ''))
    tableName = os.path.basename(input_file).split(".")[0]
    try:
        sql = "CREATE TABLE " + tableName + "("
        for colName in colList :
            sql += colName + " CHAR(20),"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)

    except:
        pass




    for i in range(1, len(csvList)) :
        rowList = csvList[i]
        sql = "INSERT INTO " +  tableName + " VALUES("
        for row in rowList:
            sql += "'" + row + "',"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)

    con.commit()


    cur.close()
    con.close()  # 데이터베이스 연결 종료

    print('Ok!')




def autoData01() :


    con = sqlite3.connect('c:/temp/userDB')
    cur = con.cursor()
    # 폴더 선택하고, 그 안의 파일목록들 추출하기.

    dirName = askdirectory()
    file_list = glob.glob(os.path.join(dirName, "*.csv"))


    for input_file in file_list:
        filereader = open(input_file, 'r', newline='')
        csvReader = csv.reader(filereader)
        colList = next(csvReader)
        tableName = os.path.basename(input_file).split(".")[0]

        try:
            sql = "CREATE TABLE " + tableName + "("
            for colName in colList:
                cList = colName.split()
                colName = ''
                for col in cList:
                    colName += col + '_'
                colName = colName[:-1]
                sql += colName + " CHAR(20),"
            sql = sql[:-1]
            sql += ')'
            cur.execute(sql)

        except:
            print('테이블 이상 -->', input_file)
            continue




        for rowList in csvReader:
            sql = "INSERT INTO " + tableName + " VALUES("
            for data in rowList:
                sql += "'" + data + "',"
            sql = sql[:-1] + ')'
            cur.execute(sql)

        filereader.close()
        con.commit()

    cur.close()
    con.close()

    print("OK!")




def autoData02() :

    con = pymysql.connect(host='192.168.98.131', user='root', password='1234', db='userDB', charset='utf8')
    cur = con.cursor()

    dirName = askdirectory()
    file_list = glob.glob(os.path.join(dirName, "*.csv"))

    for input_file in file_list:
        filereader = open(input_file, 'r', newline='')
        csvReader = csv.reader(filereader)
        colList = next(csvReader)
        tableName = os.path.basename(input_file).split(".")[0]

        try:
            sql = "CREATE TABLE " + tableName + "("
            for colName in colList:
                cList = colName.split()
                colName = ''
                for col in cList:
                    colName += col + '_'
                colName = colName[:-1]
                sql += colName + " CHAR(20),"
            sql = sql[:-1]
            sql += ')'
            cur.execute(sql)

        except:
            print('테이블 이상 -->', input_file)
            continue

        for rowList in csvReader:
            sql = "INSERT INTO " + tableName + " VALUES("
            for data in rowList:
                sql += "'" + data + "',"
            sql = sql[:-1] + ')'
            cur.execute(sql)

        filereader.close()
        con.commit()

    cur.close()
    con.close()

    print("OK!")




## 메인 코드 ##

window = Tk()

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
fileMenu.add_command(label='Excel 열기', command=openExcel)
fileMenu.add_command(label='Excel 저장', command=saveExcel)

csvMenu = Menu(mainMenu)
mainMenu.add_cascade(label='CSV 데이터 분석', menu=csvMenu)
csvMenu.add_command(label='특정 열 제거', command=csvData01)
csvMenu.add_command(label='특정 행 제거', command=csvData02)
csvMenu.add_command(label='여러 CSV 행수 알기', command=csvData03)

excelMenu = Menu(mainMenu)
mainMenu.add_cascade(label='Excel 데이터 분석', menu=excelMenu)
excelMenu.add_command(label='Excel내용 보기 - 1st', command=excelData01)
excelMenu.add_command(label='Excel내용 보기 - All', command=excelData02)
excelMenu.add_command(label='Excel내용 보기 - Select', command=excelData03)

sqliteMenu = Menu(mainMenu)
mainMenu.add_cascade(label='SQLite 데이터 분석', menu=sqliteMenu)
sqliteMenu.add_command(label='SQLite 정보 읽기', command=sqliteData01)
sqliteMenu.add_command(label='SQLite 정보 쓰기', command=sqliteData02)

mysqlMenu = Menu(mainMenu)
mainMenu.add_cascade(label='MySQL 데이터 분석', menu=mysqlMenu)
mysqlMenu.add_command(label='MySQL 정보 읽기', command=mysqlData01)
mysqlMenu.add_command(label='MySQL 정보 쓰기', command=mysqlData02)

autoMenu = Menu(mainMenu)
mainMenu.add_cascade(label='대량 데이터 처리 자동화', menu=autoMenu)
autoMenu.add_command(label='대량 CSV --> SQLite', command=autoData01)
autoMenu.add_command(label='대량 CSV --> MySQL', command=autoData02)





window.mainloop()
