

from  tkinter import *

from  tkinter.simpledialog import *

from  tkinter.filedialog import *
import csv
import json
import os
import os.path


def drawSheet(cList) :

    global cellList, csvList,input_file

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

    global  cellList, csvList,input_file
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

def openJSON() :

    global  cellList, csvList,jsonList,jsonDic,input_file


    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("JSON파일", "*.json"), ("모든파일", "*.*")))

    filereader = open(input_file, 'r', newline='',encoding='utf-8')

    jsonDic = json.load(filereader)
    csvName = jsonDic.keys()
    # dict_keys(['userTable'])
    csvName = list(jsonDic.keys())  # 딕셔너리를 리스트로 만들어줌
    # ['userTable']
    # jsonList = list(jsonDic.values())[0]                   #아래와 같은 결과
    jsonList = jsonDic[csvName[0]]
    # [{'ID': 'AAA', 'NAME': '에이', 'ADDR': '서울'}, {'ID': 'BBB', 'NAME': '삐이', 'ADDR': '경기'}, {'ID': 'CCC', 'NAME': '씨이', 'ADDR': '강원'}]

    # 헤더리스트 추출
    header_list = list(jsonList[0].keys())
    csvList.append(header_list)
    # 행들 추출: 각 딕셔너리의 값으로 행을 만듬(딕셔너리는 순서가 없기 때문에 values로 행을 추출하면 안된다: 차례가 틀릴 수 있다.)
    for tmpDic in jsonList:
        tmpList = []
        for header in header_list:
            data = tmpDic[header]  # 딕셔너리의 키에 해당하는 데이터를 data에 넣어준다: 왜??????
            tmpList.append(data)
        csvList.append(tmpList)

    drawSheet(csvList)




    filereader.close()



def  saveCSV() :
    global cellList, csvList,input_file

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
    global cellList, csvList,jsonList,jsonDic,input_file

    if csvList == [] :

        return

    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.json',

               filetypes=(("JSON파일", "*.json"), ("모든파일", "*.*")))

    filewriter = open(saveFp.name, 'w', newline='')
    #csvList ==> jsonDic
    fname =os.path.basename(input_file).split(".")[0]
    # sales_march_2014_2

    jsonDic ={}
    jsonList = []
    tmpDic = {}
    header_list = csvList[0]
    # for i in range(1,len(csvList)):
    #     rowList = csvList[1]
    #     tmpDic = {}
    #     for k in range(0,len(rowList)):
    #         tmpDic[header_list[k]]=rowList[k]
    #     jsonList.append(tmpDic)



    jsonDic[fname] = jsonList
    json.dump(jsonDic,filewriter, indent=4)
    print(jsonList)


    #보통 db의 테이블 네임을 json네임으로 사용하지만 지금은 db사용 안하기 때문에 input파일의 파일네임으로 지정

    # for  row_list  in  csvList :
    #
    #     row_str = ','.join(map(str, row_list))
    #
    #     filewriter.writelines(row_str + '\n')
    #
    #
    #
    #
    filewriter.close()





def csvData01() :
    global cellList, csvList,input_file
    csvList = []

    input_file = "d:\\data_analysis\\csv\\supplier_data.csv"

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
    global cellList, csvList,input_file
    csvList = []

    input_file = "d:\\data_analysis\\csv\\supplier_data.csv"
    filereader = open(input_file,'r', newline="")
    csvReader = csv.reader(filereader)              #csv 전용 열기
    header_list = next(csvReader)
    csvList.append(header_list)
    for row_list in csvReader:
        csvList.append(row_list)

    drawSheet(csvList)
    filereader.close()

#여러개 csv파일의 행계수 합계 궁금함.
def csvData03() :
    global cellList, csvList,input_file
    csvList = []
    dirName = askdirectory()
    #폴더에서 *.csv 파일 목록만 뽑기
    import glob
    import os
    file_list = glob.glob(os.path.join(dirName, "*.csv"))
    for input_file in file_list:
        filereader = open(input_file, 'r', newline="")
        csvReader = csv.reader(filereader)
        # header_list = next(csvReader)
        # rowCount = 0
        # for row in csvReader:
        #     rowCount +=1
        # csvList.append([os.path.basename(input_file),'-->',rowCount])
        for row in csvReader:
            csvList.append(row)
        filereader.close()
    drawSheet(csvList)

## 전역 변수 ##

csvList, cellList = [], []
jsonDic = {}
jsonList = []
input_file = ""



## 메인 코드 ##

window = Tk()
window.title('TEXT data 분석처리')
# window.geometry('600x600')



mainMenu = Menu(window)

window.config(menu=mainMenu)




fileMenu = Menu(mainMenu)

mainMenu.add_cascade(label='파일', menu=fileMenu)

fileMenu.add_command(label='CSV 열기', command=openCSV)

fileMenu.add_command(label='CSV 저장', command=saveCSV)

fileMenu.add_separator()
fileMenu.add_command(label = 'JSON 열기',command = openJSON )

fileMenu.add_command(label='JSON 저장', command=saveJSON)




csvMenu = Menu(mainMenu)

mainMenu.add_cascade(label='CSV 데이터 분석', menu=csvMenu)

csvMenu.add_command(label='특정 열,행 제거', command=csvData01)

csvMenu.add_command(label='CSV 패키지 활용', command=csvData02)
csvMenu.add_command(label='여러CSV 행수 알아내기', command=csvData03)






window.mainloop()
