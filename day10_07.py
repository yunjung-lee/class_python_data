## 영상 처리 및 데이터 분석 툴

from tkinter import *; import os.path ;import math

from  tkinter.filedialog import *

from  tkinter.simpledialog import *

import csv

import random

## 함수 선언부

def loadImage(fname) :

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    fsize = os.path.getsize(fname) # 파일 크기 확인

    inH = inW = int(math.sqrt(fsize))  # 입력메모리 크기 결정! (중요)

    inImage = []; tmpList = []

    for i in range(inH) :  # 입력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(inW) :

            tmpList.append(0)

        inImage.append(tmpList)

    # 파일 --> 메모리로 데이터 로딩

    fp = open(fname, 'rb') # 파일 열기(바이너리 모드)

    for  i  in range(inH) :

        for  k  in  range(inW) :

            inImage[i][k] =  int(ord(fp.read(1)))

    fp.close()




def openFile() :

    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH

    filename = askopenfilename(parent=window,

                               filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))

    loadImage(filename) # 파일 --> 입력메모리

    equal() # 입력메모리--> 출력메모리




import threading

def display() :

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    # 기존에 캐버스 있으면 뜯어내기.

    if  canvas != None :

        canvas.destroy()

    # 화면 준비 (고정됨)

    window.geometry(str(outH) + 'x' + str(outW))

    canvas = Canvas(window, width=outW, height=outH)

    paper = PhotoImage(width=outW, height=outH)

    canvas.create_image((outW/2, outH/2), image=paper, state='normal')

    # 화면에 출력

    def putPixel() :

        for i in range(0, outH) :

            for k in range(0, outW) :

                data = outImage[i][k]

                paper.put('#%02x%02x%02x' % (data, data, data), (k,i))




    threading.Thread(target=putPixel).start()

    canvas.pack()







def equal() :  # 동일 영상 알고리즘

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    # 중요! 출력메모리의 크기를 결정

    outW = inW;  outH = inH;

    outImage = [];   tmpList = []

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImage.append(tmpList)

    #############################

    # 진짜 영상처리 알고리즘을 구현

    ############################

    for  i  in  range(inH) :

        for  k  in  range(inW) :

            outImage[i][k] = inImage[i][k]




    display()







def addImage() :  # 밝게하기 알고리즘

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    # 중요! 출력메모리의 크기를 결정

    outW = inW;  outH = inH;

    outImage = [];   tmpList = []

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImage.append(tmpList)

    #############################

    # 진짜 영상처리 알고리즘을 구현

    ############################

    value = askinteger('밝게하기', '밝게할 값-->', minvalue=1, maxvalue=255)

    for  i  in  range(inH) :

        for  k  in  range(inW) :

            if inImage[i][k] + value > 255 :

                outImage[i][k] = 255

            else :

                outImage[i][k] = inImage[i][k] + value

    display()




def a_average() :  # 입출력 영상의 평균값

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    rawSum = 0

    for  i  in  range(inH) :

        for  k  in  range(inW) :

            rawSum += inImage[i][k]

    inRawAvg = int(rawSum / (inH*inW))




    rawSum = 0

    for  i  in  range(outH) :

        for  k  in  range(outW) :

            rawSum += outImage[i][k]

    outRawAvg = int(rawSum / (outH*outW))




    subWindow = Toplevel(window) # 부모(window)에 종속된 서브윈도

    subWindow.geometry('200x100')

    label1 = Label(subWindow, text='입력영상 평균값 -->' + str(inRawAvg) ); label1.pack()

    label2 = Label(subWindow, text='출력영상 평균값 -->' + str(outRawAvg)); label2.pack()

    subWindow.mainloop()




def upDown() :  # 상하 반전 알고리즘

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    # 중요! 출력메모리의 크기를 결정

    outW = inW;  outH = inH;

    outImage = [];   tmpList = []

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImage.append(tmpList)

    #############################

    # 진짜 영상처리 알고리즘을 구현

    ############################

    for  i  in  range(inH) :

        for  k  in  range(inW) :

            outImage[outW-1-i][k] = inImage[i][k]




    display()




def panImage() :

    global  panYN

    panYN = True




def mouseClick(event) :  # 동일 영상 알고리즘

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    global sx, sy, ex, ey, panYN

    if not panYN :

        return

    sx = event.x;  sy = event.y;




def mouseDrop(event):  # 동일 영상 알고리즘

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    global sx, sy, ex, ey, panYN

    if not panYN:

        return

    ex = event.x; ey = event.y;

    my = sx - ex ; mx = sy - ey




    # 중요! 출력메모리의 크기를 결정

    outW = inW;  outH = inH;

    outImage = [];   tmpList = []

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImage.append(tmpList)

    #############################

    # 진짜 영상처리 알고리즘을 구현

    ############################

    for  i  in  range(inH) :

        for  k  in  range(inW) :

            if 0<= i-mx <outH and 0<= k-my < outW :

                outImage[i-mx][k-my] = inImage[i][k]

    panYN = False

    display()







def zoomOut() :  # 축소하기 알고리즘

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    # 중요! 출력메모리의 크기를 결정

    scale = askinteger('축소하기', '축소할 배수-->', minvalue=2, maxvalue=32)

    outW = int(inW/scale);  outH = int(inH/scale);

    outImage = [];   tmpList = []

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImage.append(tmpList)

    #############################

    # 진짜 영상처리 알고리즘을 구현

    ############################

    for  i  in  range(inH) :

        for  k  in  range(inW) :

             outImage[int(i/scale)][int(k/scale)] = inImage[i][k]

    display()




import struct

def saveFile() :

    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH

    saveFp = asksaveasfile(parent=window, mode='wb',

                               defaultextension="*.raw", filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))

    for i in range(outW):

        for k in range(outH):

            saveFp.write( struct.pack('B',outImage[i][k]))




    saveFp.close()




def exitFile() :

    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH

    pass


def saveCSV():
    window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH


    output_file = asksaveasfile(parent=window, mode='w', defaultextension='.CSV',

               filetypes=(("CSV파일", "*.CSV"), ("모든파일", "*.*")))
    output_file = output_file.name

    header = ['Column', 'Row', 'Value']

    with open(output_file,'w', newline='') as filewriter:
        csvWriter = csv.writer(filewriter)
        csvWriter.writerow(header)



        for i in range(outW):

            for k in range(outH):
                data = outImage[i][k]
                row_list = [i, k, data]  # 화면과 실제는 x-y역전이 있다.
                csvWriter.writerow(row_list)
    print('ok')

def saveCSVshuffle():
    output_file = asksaveasfile(parent=window, mode='w', defaultextension='.CSV',

               filetypes=(("CSV파일", "*.CSV"), ("모든파일", "*.*")))
    output_file = output_file.name

    header = ['Column', 'Row', 'Value']
    rowShuffleList = []
    with open(output_file,'w', newline='') as filewriter:
        csvWriter = csv.writer(filewriter)
        csvWriter.writerow(header)



        for i in range(outW):

            for k in range(outH):
                data = outImage[i][k]
                row_list = [i, k, data]
                rowShuffleList.append(row_list)

        random.shuffle(rowShuffleList)
        for data_sh in rowShuffleList:
            csvWriter.writerow(data_sh)
    print('ok')


def loadCSV(fname) :

    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    fsize = -1
    fp=open(fname,'r')

    for f in fp:
        fsize += 1
    fp.close()
    inH = inW = int(math.sqrt(fsize))  # 입력메모리 크기 결정! (중요)

    inImage = []; tmpList = []

    for i in range(inH) :  # 입력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(inW) :

            tmpList.append(0)

        inImage.append(tmpList)

    # 파일 --> 메모리로 데이터 로딩

    fp = open(fname, 'r') # 파일 열기(바이너리 모드)

    csvFP = csv.reader(fp)
    next(csvFP)
    for row_list in csvFP:
        row = int(row_list[0])
        col = int(row_list[1])
        value = int(row_list[2])
        inImage[row][col]=value
    fp.close()



def openCSV() :

    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH

    filename = askopenfilename(parent=window,

                               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))

    loadCSV(filename) # 파일 --> 입력메모리

    equal() # 입력메모리--> 출력메모리

import sqlite3
def saveSQLite() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    global csvList, input_file

    con = sqlite3.connect('c:/temp/userDB')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    # 열이름 리스트 만들기
    colList = []

    fname = os.path.basename(filename).split(".")[0]
    try:

        sql = "CREATE TABLE imageTable(filename char(20), resolution smallint" +", row smallint, col smallint, value smallint) "

        cur.execute(sql)

    except:

        pass




    for i in range(inW) :
        for k in range(inH):
           sql = "INSERT INTO imageTable VALUES('" + fname + "',"+str(inW)+"," +str(i)+","+str(k)+","+str(inImage[i][k])+")"
           cur.execute(sql)




    con.commit()




    cur.close()

    con.close()  # 데이터베이스 연결 종료

    print('Ok!')



## 전역 변수부

window, canvas, paper, filename = [None] * 4

inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4

panYN = False;  sx, sy, ex, ey = [0] * 4




## 메인 코드부

window = Tk();  window.geometry('200x200');

window.title('영상 처리&데이터 분석 Ver 0.3')

window.bind("<Button-1>", mouseClick)

window.bind("<ButtonRelease-1>", mouseDrop)




mainMenu = Menu(window);window.config(menu=mainMenu)

fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)

fileMenu.add_command(label='열기', command=openFile)

fileMenu.add_command(label='저장', command=saveFile)

fileMenu.add_separator()

fileMenu.add_command(label='종료', command=exitFile)




pixelMenu = Menu(mainMenu);mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)

pixelMenu.add_command(label='동일영상', command=equal)

pixelMenu.add_command(label='밝게하기', command=addImage)




geoMenu = Menu(mainMenu);mainMenu.add_cascade(label='기하학 처리', menu=geoMenu)

geoMenu.add_command(label='상하반전', command=upDown)

geoMenu.add_command(label='화면이동', command=panImage)

geoMenu.add_command(label='화면축소', command=zoomOut)




analyzeMenu = Menu(mainMenu);mainMenu.add_cascade(label='데이터분석', menu=analyzeMenu)

analyzeMenu.add_command(label='평균값', command=a_average)


otherMenu = Menu(mainMenu);mainMenu.add_cascade(label='다른 포맷 처리', menu=otherMenu)
otherMenu.add_command(label = 'CSV 저장',command = saveCSV)
otherMenu.add_command(label = 'CSV 셔플 저장',command = saveCSVshuffle)
otherMenu.add_command(label = 'CSV 불러오기',command = openCSV)
otherMenu.add_separator()
otherMenu.add_command(label = 'SQLite로 저장', command = saveSQLite)

window.mainloop()


