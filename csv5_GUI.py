
from  tkinter import *

from  tkinter.simpledialog import *

from  tkinter.filedialog import *




def drawSheet(cList) :

    global cellList

    if cellList != None :

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

    global  csvList

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

        row_list = row.split(',')

        csvList.append(row_list)




    drawSheet(csvList)




    filereader.close()




def  saveCSV() :

    global csvList

    if csvList == [] :

        return

    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv',

               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))

    filewriter = open(saveFp.name, 'w', newline='')

    for  row_list  in  csvList :

        row_str = ','.join(map(str, row_list))

        filewriter.writelines(row_str + '\n')




    filewriter.close()




def csvData01() :

    global  csvList

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




## 전역 변수 ##

csvList, cellList = [], []




## 메인 코드 ##

window = Tk()




mainMenu = Menu(window)

window.config(menu=mainMenu)




fileMenu = Menu(mainMenu)

mainMenu.add_cascade(label='파일', menu=fileMenu)

fileMenu.add_command(label='CSV 열기', command=openCSV)

fileMenu.add_command(label='CSV 저장', command=saveCSV)




csvMenu = Menu(mainMenu)

mainMenu.add_cascade(label='CSV 데이터 분석', menu=csvMenu)

csvMenu.add_command(label='특정 열,행 제거', command=csvData01)

window.mainloop()
