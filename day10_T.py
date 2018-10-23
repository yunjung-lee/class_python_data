# (1) 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리)
#
# (2) 텍스트마이닝 기반 데이터 분석 (부제: 텍스트 기반 데이터 분석 및 처리)
#
# (3) 빅데이터 분석 결과 시각화 (부제 : 데이터베이스 기반 데이터 분석 및 GUI 시각화)
#
#
# 복습퀴즈1. 선택한 폴더의 모든 엑셀 파일을 SQLite의 테이블로 입력되는
#
#               코드를 작성하세요. (별도의 소스코드에 작성)
#
#
# 복습퀴즈2. SQLite의 모든 테이블이 선택한 폴더의 엑셀 파일로 저장되는
#
#               코드를 작성하세요. (별도의 소스코드에 작성)
#
#
#
# 어제 과제 : [SQLite에서 불러오기]
#
#     --> 영상 목록이 출력되고 (cat01:128 ....)
#
#  선택하면 화면에 로딩


from tkinter import *

import os.path ;import math

from  tkinter.filedialog import *

from  tkinter.simpledialog import *

import csv

import random

import json

import os

import os.path

import xlrd

import xlwt

import sqlite3

import pymysql

import glob


## 전역 변수부

window, canvas, paper, filename = [None] * 4

inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4

panYN = False;  sx, sy, ex, ey = [0] * 4


## 메인 코드부
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

def saveImageSqlite():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global csvList, input_file

    con = sqlite3.connect('c:/temp/userDB')
    cur = con.cursor()

    fname = os.path.basename(filename).split(".")[0]
    try:
        sql = "create table ImageTable(filename char(20) resolution smallint, row smallint, col smallint, value smallint)"
        cur.execute(sql)

    except :
        pass

    for i in range(inW) :
        for k in range(inH):
            sql = "insert into ImageTable values('" + fname+"','"+str(inW)+"','"+str(i)+"','"+str(k)+"','"+str(inImage[i][k])+"')"
            cur.execute(sql)

    con.commit()
    cur.close()                         #con 보다 앞에서 닫아야 한다.
    con.close()

    print('ok-sql')

def saveImageExcel2():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global csvList, input_file

    if outImage == []:
        return

    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.xls',

                           filetypes=(("Excel파일", "*.xls"), ("모든파일", "*.*")))
    fileName = saveFp.name

    outWorkbook = xlwt.Workbook()                                                              #Workbook :  excel file
    outSheet = outWorkbook.add_sheet('sheet1')                                          #이름을 추후에 지정

    for i in range (len(outImage)):
        for k in range(len(outImage[i])):
            outSheet.write(i,k,outImage[i][k])

    outWorkbook.save(fileName)
    print('ok-excel')


def saveImageExcel():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global csvList, input_file

    if inImage == []:
        return

    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.xls',

                           filetypes=(("Excel파일", "*.xls"), ("모든파일", "*.*")))
    fileName = saveFp.name

    outWorkbook = xlwt.Workbook()                                                              #Workbook :  excel file
    outSheet = outWorkbook.add_sheet('sheet1')



    outWorkbook.save(fileName)
    print('ok-excel')

window = Tk()

window.title('영상 처리 & 통계')

window.bind("<Button-1>", mouseClick)
window.bind("<ButtonRelease-1>", mouseDrop)








mainMenu = Menu(window)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

window.configure(menu = mainMenu)
imageSqliteMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "SQLite 이미지", menu = imageSqliteMenu)
imageSqliteMenu.add_command(label = "SQLite 저장", command = saveImageSqlite)
imageSqliteMenu.add_command(label = "엑셀 저장", command = saveImageExcel)




window.mainloop()



























































































































































































