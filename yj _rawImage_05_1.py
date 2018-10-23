############################################################################
# ** 디지털 영상 처리 (Digital Image Processing) 알고리즘 **
#
#
#
#
# (1) 화소점 처리 (Pixel Processing) : 한개 점을 처리하기, 화소값이 변경
#
#    동일영상, 화소값반전, 밝게하기(덧셈연산), 어둡게(뺄셈), 곱셈,
#
#  나눗셈, 파라볼라(Cap, Cup), 감마, 이진화, 특정범위 추출,
#
# (2) 기하학 처리(Geometry Processing) : 한개 점을 처리. 화소값은 그대로, 위치변경
#
#     상하반전, 좌우반전, 이동, 회전, 확대, 축소, 영상 합성
#
# (3) 화소영역 처리 (Area Processing) : 여러개 점이 관련되어 처리.
#
#     엠보싱, 블러링, 샤프닝, 에지검색(종류 수십개), 잡음제거
#########################################################################################


from tkinter import  *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import os.path
import math
import operator
import struct
from statistics import median
import matplotlib.pyplot as plt
import csv
import sqlite3
import pymysql
import xlwt
import xlsxwriter





#변수
fSize = 0
fName = 0
inH, inW, outW, outH,sx,sy,ex,ey = 0,0,0,0,0,0,0,0
inImageList,tmpList ,outImageList,rList= [],[],[],[]
penYN = False
fileName ,window, canvas, paper= [None] * 4


#함수
def openfile():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList,  outImageList,tmpList,rList,fileName, window, canvas, paper
    fileName = askopenfilename(parent = window, filetype = (('RAW파일','*.raw'),('모든파일','*.*')))
    loadImage(fileName)
    equal()

def dummy_in():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper
    for i in range(inW):
        tmpList = []
        for k in range(inH):
            tmpList.append(0)
        rList.append(tmpList)

def dummy_out():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper
    rList=[]
    for i in range(outW):
        tmpList = []
        for k in range(outH):
            tmpList.append(0)
        rList.append(tmpList)

def loadImage(fName):
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN,inImageList, outImageList,tmpList,rList,fileName, window, canvas, paper
    fSize = os.path.getsize(fName)
    inH = inW = int(math.sqrt(fSize))
    inImageList = []
    dummy_in()
    inImageList=rList

    fp = open(fName, 'rb')
    for i in range(inW):
        for k in range(inH):
            inImageList[i][k]=int(ord(fp.read(1)))                  # ord(fp.read(1))=?
    fp.close()

def equal():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper,rList
    outW=inW
    outH=inH
    dummy_out()
    outImageList = rList
    for i in range(inW):
        for k in range(inH):
            outImageList[i][k]=inImageList[i][k]
    display()

def display():
    global  inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper
    if canvas != None:
        canvas.destroy()
    window.geometry(str(outW*2)+'x'+str(outH*2))
    canvas = Canvas(window, width = outW, height = outH)

    paper = PhotoImage(width = outW, height = outH)

    canvas.create_image((outW / 2, outH / 2), image=(paper), state='normal',anchor=CENTER)
    for i in range(outW):
        for k in range(outH):
            data = outImageList[i][k]
            paper.put('#%02x%02x%02x' % (data, data, data) ,(k,i) )
    canvas.pack(expand=1)

def r_display():
    global  inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper
    if canvas != None:
        canvas.destroy()
    window.geometry(str(outW*2)+'x'+str(outH*2))
    canvas = Canvas(window, width = outW*2, height = outH*2)

    paper = PhotoImage(width = outW, height = outH)

    canvas.create_image((outW / 2, outH / 2), image=(paper), state='normal',anchor=CENTER)
    for i in range(outW):
        for k in range(outH):
            data = outImageList[i][k]
            paper.put('#%02x%02x%02x' % (data, data, data) ,(k,i) )
    canvas.pack()


def savefile():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    saveFp = asksaveasfile(parent = window,mode='wb',defaultextension = "*.raw",filetype = (('RAW파일','*.raw'),('모든파일','*.*')) )

    for i in range(outW):
        for k in range(outH):
            saveFp.write(struct.pack('B',outImageList[i][k]))
    saveFp.close()


def bright():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper
    outW=inW
    outH=inH
    dummy_out()
    outImageList=rList
    value = askinteger('밝게하기', '밝게 할 값 : ', minvalue = 1,maxvalue = 255)
    for i in range(outW):
        for k in range(outH):
            if inImageList[i][k] + value >255:
                inImageList[i][k] = 255
            else:
                outImageList[i][k]= inImageList[i][k] + value

    display()


def dark():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper
    outW=inW
    outH=inH
    dummy_out()
    outImageList=rList
    value = askinteger('어둡게하기', '어둡게 할 값 : ', minvalue = 1,maxvalue = 255)
    for i in range(outW):
        for k in range(outH):
            if inImageList[i][k] + value <0 :
                inImageList[i][k] = 0
            else:
                outImageList[i][k]= inImageList[i][k] - value

    display()

def revers():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    outW=inW
    outH=inH
    dummy_out()
    outImageList=rList
    for i in range(outW):
        for k in range(outH):
            outImageList[i][k] = 255-inImageList[i][k]
    display()

def multi():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    outW=inW
    outH=inH
    dummy_out()
    outImageList=rList
    value = askinteger('곱하기', '곱할 값 : ', minvalue=2, maxvalue=255)
    for i in range(outW):
        for k in range(outH):
            if inImageList[i][k] + value > 255 :
                inImageList[i][k] = 255
            else:
                outImageList[i][k] = inImageList[i][k]*value
    display()

def div():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    outW=inW
    outH=inH
    dummy_out()
    outImageList=rList
    value = askinteger('나누기', '나눌 값 : ', minvalue=2, maxvalue=255)
    for i in range(outW):
        for k in range(outH):
            outImageList[i][k] = int(inImageList[i][k]/value)
    display()

def gamma():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    outW=inW
    outH=inH
    dummy_out()
    outImageList=rList
    value = askinteger('감마연산인자', '감마 상수(감마상수의 10배인 정수 : 2~10) : ', minvalue=2, maxvalue=10)
    for i in range(outW):
        for k in range(outH):
            outImageList[i][k] = int(inImageList[i][k]**(value/10))
    display()

def mc(event1):
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    if sx and sy == 0:
        print("마우스를 클릭하세요.")
        return
    else:
        sx=event1.x
        sy=event1.y
        print("현재 클릭한 좌표는: ", sx, " ", sy)


def binary():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    outW = inW
    outH = inH
    dummy_out()
    outImageList = rList
    value = askinteger('threshold', 'threshold 상수(1~255) : ', minvalue=1, maxvalue=255)
    for i in range(outW):
        for k in range(outH):
            if inImageList[i][k] > value:
                outImageList[i][k] = 255
            else:
                outImageList[i][k] = 0
    display()
    print('done')

def zoomIn():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    value = askinteger('확대', '확대비율(2~16) : ', minvalue=2, maxvalue=10)
    outW=inW*value
    outH=inH*value
    dummy_out()
    outImageList=rList
    for i in range(outW):
        for k in range(outH):
            outImageList[i][k]=inImageList[int(i/value)][int(k/value)]
    display()

def zoomOut():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    value = askinteger('축소', '축비율(2의 제곱수 : 2~16) : ', minvalue=2, maxvalue=16)
    outW=int(inW/value)
    outH=int(inH/value)
    dummy_out()
    outImageList=rList
    for i in range(inW):
        for k in range(inH):
            outImageList[int(i / value)][int(k / value)] = inImageList[i][k]
    display()

def upDown():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    outW=inW
    outH=inH
    dummy_out()
    outImageList=rList
    for i in range(inW):
        for k in range(inH):
            outImageList[outH-1-i][k] = inImageList[i][k]
    display()

def leftRight():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    outW=inW
    outH=inH
    dummy_out()
    outImageList=rList
    for i in range(inW):
        for k in range(inH):
            outImageList[i][outH-1-k] = inImageList[i][k]
    display()

def move():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    penYN = True


def mouseClick(event):
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    if not penYN:
        return
    sx=event.x
    sy=event.y


def mouseMove(event):
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    if not penYN:
        return
    ex=event.x
    ey=event.y
    mx = sx-ex
    my = sy-ey
    outW=inW
    outH=inH
    outImageList = []
    dummy_out()
    outImageList=rList
    for i in range(inW):
        for k in range(inH):
            if 0< k-my < outH and 0< i-mx <outW:
                outImageList[i-mx][k-my] = inImageList[i][k]

    penYN=False
    display()

def rotate():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
    value = askinteger('각도', '회전각도(90=1,180=2,270=3) : ', minvalue=1, maxvalue=3)
    outW = inW
    outH = inH
    dummy_out()
    outImageList = rList
    for i in range(inW):
        for k in range(inH):
            if value==1:
                outImageList[k][outH - 1 - i] = inImageList[i][k]
            elif value==2:
                outImageList[outH - 1 - i][outW - 1 - k] = inImageList[i][k]
            else:
                outImageList[outW - 1 - k][i] = inImageList[i][k]
    display()

def overlap():
    global newImage,oldImage,inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage
    oldName = askopenfilenames(parent = window, filetype = (('RAW파일','*.raw'),('모든파일','*.*')))
    oldName = oldName[0]                        #튜플로 열림 왜인지 모르겠음

    fsize = os.path.getsize(oldName)
    inH = inW = int(math.sqrt(fsize))
    oldImage = []
    for i in range(inH):
        tmpList = []
        for k in range(inW):
            tmpList.append(0)
        oldImage.append(tmpList)
    fp = open(oldName, 'rb')
    for i in range(inH):
        for k in range(inW):
            oldImage[i][k] = int(ord(fp.read(1)))

    newName = askopenfilenames(parent=window, filetype=(('RAW파일', '*.raw'), ('모든파일', '*.*')))
    newName = newName[0]
    fsize = os.path.getsize(newName)
    inH = inW = int(math.sqrt(fsize))
    newImage = []
    for i in range(inH):
        tmpList = []
        for k in range(inW):
            tmpList.append(0)
        newImage.append(tmpList)
    fp = open(newName, 'rb')
    for i in range(inH):
        for k in range(inW):
            newImage[i][k] = int(ord(fp.read(1)))
    outW=inW
    outH=inH
    dummy_out()
    outImageList = rList
    for i in range(inW):
        for k in range(inH):
            outImageList[i][k]=int((oldImage[i][k]+newImage[i][k])/2)
    display()


def embossing() :  # 엠보싱

    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage,value

    outW = inW;  outH = inH

    outImageList,tmpList = [],[]

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImageList.append(tmpList)

    MSIZE = 3
    mask = [[-1,0,0],[0,0,0],[0,0,1]]

    tmpInImage = []

    for  i  in  range(inH + 2) :
        tmpList = []
        for  k  in  range(inW + 2) :
            tmpList.append(0)
        tmpInImage.append(tmpList)

    tmpOutImage = []

    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpOutImage.append(tmpList)

    #원래 입력 --> 임시 입력
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i+1][k+1] = inImageList[i][k]

    #회선연산하기 , 마스크로 쭉 긁으면서 계산하기
    for i in range(1,inH):
        for k in range(1,inW):
            S = 0.0
            for m in range(0, MSIZE):
                for n  in  range(0,MSIZE):
                    S +=mask[m][n]*tmpInImage [i+(m-1)][k + (n-1)]
            tmpOutImage[i-1][k-1] = S

    #127더해주기 (마스크의 합계가 0인 경우)
    for i in range(outW) :
        for k in range(outH) :
            tmpOutImage[i][k] =+127

    #임시 출력 --> 원래 출력
    for i in range(outW) :
        for k in range(outH) :

            value = int(tmpOutImage[i][k])

            if value > 225 :
                value = 255
            elif value <0 :
                value = 0
            else:
                outImageList[i][k] = value


    display()


def blurr() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    outW = inW;
    outH = inH
    outImageList, tmpList = [], []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageList.append(tmpList)

    MSIZE = 3
    mask = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]

    tmpInImage = []
    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpInImage.append(tmpList)

    tmpOutImage = []
    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpOutImage.append(tmpList)

    # 원래 입력 --> 임시 입력
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImageList[i][k]

    # 회선연산하기 , 마스크로 쭉 긁으면서 계산하기
    for i in range(1, inH):
        for k in range(1, inW):
            S = 0.0
            for m in range(0, MSIZE):
                for n in range(0, MSIZE):
                    S += mask[m][n] * tmpInImage[i + (m - 1)][k + (n - 1)]
            tmpOutImage[i - 1][k - 1] = S
    #
    # # 127더해주기 (마스크의 합계가 0인 경우)
    # for i in range(outW):
    #     for k in range(outH):
    #         tmpOutImage[i][k] = +127

    # 임시 출력 --> 원래 출력
    for i in range(outW):
        for k in range(outH):
            value = int(tmpOutImage[i][k])
            if value > 225:
                value = 255
            elif value < 0:
                value = 0
            else:
                outImageList[i][k] = value

    display()


def gaussian() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    outW = inW;
    outH = inH
    outImageList, tmpList = [], []

    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageList.append(tmpList)

    MSIZE = 3
    mask = [[1/16,1/8,1/16],[1/8,1/4,1/8],[1/16,1/8,1/16]]

    tmpInImage = []
    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpInImage.append(tmpList)

    tmpOutImage = []
    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpOutImage.append(tmpList)

    # 원래 입력 --> 임시 입력
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImageList[i][k]

    # 회선연산하기 , 마스크로 쭉 긁으면서 계산하기
    for i in range(1, inH):
        for k in range(1, inW):
            S = 0.0
            for m in range(0, MSIZE):
                for n in range(0, MSIZE):
                    S += mask[m][n] * tmpInImage[i + (m - 1)][k + (n - 1)]
            tmpOutImage[i - 1][k - 1] = S

    # # 127더해주기 (마스크의 합계가 0인 경우,마스크의 합계가 1인 경우 필요없음)
    # for i in range(outW):
    #     for k in range(outH):
    #         tmpOutImage[i][k] = +127

    # 임시 출력 --> 원래 출력
    for i in range(outW):
        for k in range(outH):

            value = int(tmpOutImage[i][k])

            if value > 225:
                value = 255
            elif value < 0:
                value = 0
            else:
                outImageList[i][k] = value

    display()
    print('ok')



def Sharp() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    outW = inW;
    outH = inH
    outImageList, tmpList = [], []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageList.append(tmpList)

    MSIZE = 3
    mask = [[-1,-1,-1],[-1,9,-1],[-1,-1,-1]]

    tmpInImage = []
    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpInImage.append(tmpList)

    tmpOutImage = []
    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpOutImage.append(tmpList)

    # 원래 입력 --> 임시 입력
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImageList[i][k]

    # 회선연산하기 , 마스크로 쭉 긁으면서 계산하기
    for i in range(1, inH):
        for k in range(1, inW):
            S = 0.0
            for m in range(0, MSIZE):
                for n in range(0, MSIZE):
                    S += mask[m][n] * tmpInImage[i + (m - 1)][k + (n - 1)]
            tmpOutImage[i - 1][k - 1] = S

    # # 127더해주기 (마스크의 합계가 0인 경우,마스크의 합계가 1인 경우 필요없음)
    # for i in range(outW):
    #     for k in range(outH):
    #         tmpOutImage[i][k] = +127

    # 임시 출력 --> 원래 출력
    for i in range(outW):
        for k in range(outH):
            value = int(tmpOutImage[i][k])
            if value > 225:
                value = 255
            elif value < 0:
                value = 0
            else:
                outImageList[i][k] = value

    display()
    print('ok')


def Unsharp_Masking():
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    outW = inW;
    outH = inH
    outImageList, tmpList = [], []
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageList.append(tmpList)

    MSIZE = 3
    mask = [[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]]

    tmpInImage = []
    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpInImage.append(tmpList)

    tmpOutImage = []
    for i in range(inH + 2):
        tmpList = []
        for k in range(inW + 2):
            tmpList.append(0)
        tmpOutImage.append(tmpList)

    # 원래 입력 --> 임시 입력
    for i in range(inH):
        for k in range(inW):
            tmpInImage[i + 1][k + 1] = inImageList[i][k]

    # 회선연산하기 , 마스크로 쭉 긁으면서 계산하기
    for i in range(1, inH):
        for k in range(1, inW):
            S = 0.0
            for m in range(0, MSIZE):
                for n in range(0, MSIZE):
                    S += (1-mask[m][n]) * tmpInImage[i + (m - 1)][k + (n - 1)]
            tmpOutImage[i - 1][k - 1] = S

    for i in range(outW):
        for k in range(outH):
            value = int(tmpOutImage[i][k])
            if value > 225:
                value = 255
            elif value < 0:
                value = 0
            else:
                outImageList[i][k] = value

    display()
    print('ok')

def exitfile():
    window.quit()
    window.destroy()




def a_average() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    rawSum, rawMax, rawMin, rawMeadian = 0, 0, 0, 0
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            rawSum += inImageList[i][k]
    inRawAvg = int(rawSum / (inH*inW))
    inRawAvg = int(rawSum / (inH * inW))
    rawMax = max(map(max, inImageList))
    rawMin = min(map(min, inImageList))
    rawMedian = int(median(map(median, inImageList)))
    rawSum = 0
    for  i  in  range(outH) :
        for  k  in  range(outW) :
            rawSum += outImageList[i][k]
    outRawAvg = int(rawSum / (outH*outW))

    subWindow = Toplevel(window) # 부모(window)에 종속된 서브윈도
    subWindow.geometry('200x100')
    label1 = Label(subWindow, text='입력영상 합계 -->' + str(rawSum))
    label1.pack()
    label2 = Label(subWindow, text='입력영상 평균값 -->' + str(inRawAvg))
    label2.pack()
    label3 = Label(subWindow, text='입력영상 최댓값 -->' + str(rawMax))
    label3.pack()
    label4 = Label(subWindow, text='입력영상 최소값 -->' + str(rawMin))
    label4.pack()
    label5 = Label(subWindow, text='입력영상 중위수 -->' + str(rawMedian))
    label5.pack()
    subWindow.mainloop()


def a_histogram() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    normalList = [0]*256
    countList = [0]*256

    for i in range(outH):
        for k in range(outW):
            value = outImageList[i][k]
            countList[value] += 1

    maxVal = max(countList)
    minVal = min(countList)

    for i in range(len(countList)):
        normalList[i] = (countList[i] - minVal)*256/(maxVal-minVal)

    subWindow = Toplevel(window)
    subWindow.geometry('256x256')
    subCanvas = Canvas(subWindow, width = 256, height = 256)
    subPaper =  PhotoImage(width = 256, height = 256)
    subCanvas.create_image((256/2,256/2), image = subPaper, state = 'normal')

    for i in range(0,256) :
        for k in range(0, int(normalList[i])):
            data = 0
            subPaper.put('#%02x%02x%02x' % (data,data,data),(i,255-k))

    subCanvas.pack(expand = 1, anchor = CENTER)
    subWindow.mainloop()


def a_histogram2() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    countList = [0]*256
    for i in range(outH):
        for k in range(outW):
            value = outImageList[i][k]
            countList[value] += 1

    plt.plot(countList)
    plt.show()



def a_endInSearch() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    outW = inW;  outH = inH
    outImageList = [];   tmpList = []
    value = 0
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageList.append(tmpList)

     # 진짜 영상처리 알고리즘을 구현

    maxVal , minVal , HIGH= 0,255,255
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            data = inImageList[i][k]
            if data > maxVal:
                maxVal = data
            if data < minVal :
                minVal = data
    limit = askinteger("앤드인"," 상하 범위 : ",minvalue = 1, maxvalue = 127)
    maxVal -= limit
    minVal += limit
    #히스토그램 스트래칭
    #new = (old - min) * HIGH / (max-min) : 정규화 공식과 비슷하다
    # out = (in - min) * HIGH / (max-min)
    for i in range(inH):
        for k in range(inW):
            value =  int( (inImageList[i][k] - minVal) * HIGH / (maxVal-minVal))
            if value<0:
                value = 0
            if value>255:
                value =255
            outImageList[i][k]  =value

    display()


def a_histoStretch() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    outW = inW;  outH = inH
    outImageList = [];   tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageList.append(tmpList)

    # 진짜 영상처리 알고리즘을 구현
    maxVal , minVal , HIGH= 0,255,255
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            data = inImage[i][k]
            if data > maxVal:
                maxVal = data
            if data < minVal :
                minVal = data
    for i in range(inH):
        for k in range(inW):
            value =  int( (inImageList[i][k] - minVal) * HIGH / (maxVal-minVal))
            if value<0:
                value = 0
            if value>255:
                value =255
            outImageList[i][k]  =value

    display()



def a_histoEqual():
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    outW = inW
    outH = inH
    outImageList = []
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageList.append(tmpList)
    # 진짜 영상처리 알고리즘을 구현
    histo = [0]*255
    sumHisto = [0]*255
    normalHisto = [0]*255
    HIGH =  255

    #히스토그램 작성
    for i in range(inH):
        for k in range(inW):
            value = inImageList[i][k]
            histo[value] += 1
    #누적 히스토그램 작성
    sVal = 0
    for i in range(len(histo)):
        sVal += histo[i]
        sumHisto[i] = sVal
    #정규화된 누적 히스토그램  : (누적합/ ( 행개수*열개수)) * HIGH
    for i in range(len(sumHisto)) :
        normalHisto[i] = int(sumHisto[i] / (outW * outH) * HIGH)

    #정규화된 값으로 출력하기
    for i in range(inH):
        for k in range(inW):
            index = inImageList[i][k]
            outImageList[i][k] = normalHisto[index]


    display()




def saveCSV() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    output_file = asksaveasfile(parent=window, mode='w', defaultextension="*.csv", filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))
    output_file = output_file.name

    header = ['Column', 'Row', 'Value']

    with open(output_file, 'w', newline='') as filewriter:
        csvWriter = csv.writer(filewriter)
        csvWriter.writerow(header)
        for row in range(outW):
            for col in range(outH):
                data = outImageList[row][col]
                row_list = [row, col, data]
                csvWriter.writerow(row_list)



def loadCSV(fname) :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    fsize = -1
    fp = open(fname, 'r')
    for  f  in fp :
        fsize += 1
    fp.close()
    inH = inW = int(math.sqrt(fsize))
    inImageList = []

    for i in range(inH) :
        tmpList = []
        for k in range(inW) :
            tmpList.append(0)
        inImageList.append(tmpList)


    fp = open(fname, 'r')
    csvFP = csv.reader(fp)
    next(csvFP)
    for row_list in csvFP :
        row= int(row_list[0]) ; col = int(row_list[1]) ; value=int(row_list[2])
        inImageList[row][col] = value

    fp.close()




def openCSV() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    filename = askopenfilename(parent=window,filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))

    loadCSV(filename)

    equal()






def saveSQLite() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value

    con = sqlite3.connect('imageDB')
    cur = con.cursor()


    colList = []
    fname = os.path.basename(filename).split(".")[0]
    try:
        sql = "CREATE TABLE imageTable( filename CHAR(20), resolution smallint" + ", row  smallint,  col  smallint, value  smallint)"
        cur.execute(sql)
    except:
        pass


    for i in range(inW) :
        for k in range(inH) :
            sql = "INSERT INTO imageTable VALUES('" + fname + "'," + str(inW) +"," + str(i) + "," + str(k) + "," + str(inImage[i][k]) +")"
            cur.execute(sql)

    con.commit()
    cur.close()
    con.close()  # 데이터베이스 연결 종료

    print('Ok!')




def openSQLite() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    con = sqlite3.connect('imageDB')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
    try :
        sql = "SELECT DISTINCT filename, resolution FROM imageTable"
        cur.execute(sql)
        tableNameList = []
        while True :
            row = cur.fetchone()
            if row == None :
                break
            tableNameList.append( row[0] + ':' + str(row[1]) )


        def selectTable() :
            global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
            selectedIndex = listbox.curselection()[0]
            subWindow.destroy()
            fname, res = tableNameList[selectedIndex].split(':')
            filename = fname
            sql = "SELECT row, col, value FROM imageTable WHERE filename='" +fname + "' AND resolution=" + res
            print(sql)
            cur.execute(sql)

            inH = inW = int(res)
            inImageList = [];  tmpList = []
            for i in range(inH):  # 입력메모리 확보(0으로 초기화)
                tmpList = []
                for k in range(inW):
                    tmpList.append(0)
                inImageList.append(tmpList)

            while True :
                row_tuple = cur.fetchone()
                if row_tuple == None :
                    break

                row, col, value = row_tuple
                inImageList[row][col] = value

            cur.close()
            con.close()
            equal()

            print("Ok! openSQLite")



        subWindow = Toplevel(window)
        listbox = Listbox(subWindow)
        button = Button(subWindow, text='선택', command=selectTable)
        listbox.pack(); button.pack()
        for sName in tableNameList :
            listbox.insert(END, sName)
        subWindow.lift()

    except :

        cur.close()
        con.close()
        print("Error! openSQLite")






def saveMySQL() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value,filename
    con = pymysql.connect(host='192.168.98.131', user='root', password='1234', db='imageDB', charset='utf8')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

    colList = []
    fname = os.path.basename(filename).split(".")[0]
    try:
        sql = "CREATE TABLE imageTable( filename CHAR(20), resolution smallint" + ", row  smallint,  col  smallint, value  smallint)"
        cur.execute(sql)
    except:
        pass

    try:
        sql = "DELETE FROM imageTable WHERE filename='" +fname + "' AND resolution=" + str(outW)
        cur.execute(sql)
        con.commit()

    except:
        pass

    for i in range(inW) :
        for k in range(inH) :
            sql = "INSERT INTO imageTable VALUES('" + fname + "'," + str(outW) +"," + str(i) + "," + str(k) + "," + str(outImageList[i][k]) +")"
            cur.execute(sql)

    con.commit()

    cur.close()
    con.close()  # 데이터베이스 연결 종료

    print('Ok! saveMySQL')




def openMySQL() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    con = pymysql.connect(host='192.168.98.131', user='root', password='1234', db='imageDB', charset='utf8')  # 데이터베이스 지정(또는 연결)
    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

    try :
        sql = "SELECT DISTINCT filename, resolution FROM imageTable"
        cur.execute(sql)
        tableNameList = []
        while True :
            row = cur.fetchone()
            if row == None :
                break

            tableNameList.append( row[0] + ':' + str(row[1]) )

        def selectTable() :
            global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
            selectedIndex = listbox.curselection()[0]
            subWindow.destroy()
            fname, res = tableNameList[selectedIndex].split(':')
            filename = fname
            sql = "SELECT row, col, value FROM imageTable WHERE filename='" +fname + "' AND resolution=" + res
            print(sql)
            cur.execute(sql)

            inH = inW = int(res)
            inImageList = [];  tmpList = []
            for i in range(inH):  # 입력메모리 확보(0으로 초기화)
                tmpList = []
                for k in range(inW):
                    tmpList.append(0)
                    inImageList.append(tmpList)

            while True :
                row_tuple = cur.fetchone()
                if row_tuple == None :
                    break
                row, col, value = row_tuple
                inImageList[row][col] = value

            cur.close()
            con.close()
            equal()

            print("Ok! openMySQL")



        subWindow = Toplevel(window)
        listbox = Listbox(subWindow)
        button = Button(subWindow, text='선택', command=selectTable)
        listbox.pack(); button.pack()
        for sName in tableNameList :
            listbox.insert(END, sName)
        subWindow.lift()


    except :
        cur.close()
        con.close()

        print("Error! openMySQL")




def saveExcel1() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    output_file = asksaveasfile(parent=window, mode='w', defaultextension="*.xls", filetypes=(("XLS파일", "*.xls"), ("모든파일", "*.*")))
    output_file = output_file.name

    sheetName = os.path.basename(output_file).split(".")[0]
    wb = xlwt.Workbook()
    ws = wb.add_sheet(sheetName)

    for rowNum in range(outH):
        for colNum in range(outW):
            data = outImageList[rowNum][colNum]
            ws.write(rowNum, colNum, data)

    wb.save(output_file)

    print('OK! saveExcel1')




def saveExcel2() :
    global newImage, oldImage, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper, inImage, value
    output_file = asksaveasfile(parent=window, mode='w',defaultextension="*.xlsx", filetypes=(("XLSX파일", "*.xls"), ("모든파일", "*.*")))
    output_file = output_file.name

    sheetName = os.path.basename(output_file).split(".")[0]
    wb = xlsxwriter.Workbook(output_file)
    ws = wb.add_worksheet(sheetName)

    ws.set_column(0, outW, 1.0)
    for r in range(outH):
        ws.set_row(r, 9.5)

    for  rowNum in range(outW) :
        for colNum in range(outH) :
            data = outImageList[rowNum][colNum]
            if data > 15 :
                hexStr = '#' + (hex(data)[2:])*3
            else :
                hexStr = '#' + ('0' + hex(data)[2:]) * 3

            cell_format = wb.add_format()
            cell_format.set_bg_color(hexStr)

            ws.write(rowNum, colNum, '', cell_format)

    wb.close()

    print('OK! saveExcel2')



#메인

window = Tk()
window.geometry('800x600')
window.title('Image Ver.0.01 ')
window.bind('<Button-1>',mouseClick)
window.bind('<ButtonRelease-1>',mouseMove)


mainMenu = Menu(window)
window.configure(menu = mainMenu)

filemenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = filemenu)
filemenu.add_command(label = '열기', command = openfile)
filemenu.add_separator()
filemenu.add_command(label = '저장', command = savefile)
filemenu.add_separator()
filemenu.add_command(label = '종료', command = exitfile)

pixelmenu = Menu(mainMenu)
mainMenu.add_cascade(label = '화소점 처리', menu = pixelmenu)
pixelmenu.add_command(label = "밝게", command = bright)
pixelmenu.add_command(label = "어둡게", command = dark)
pixelmenu.add_separator()
pixelmenu.add_command(label = "화소반전", command = revers)
pixelmenu.add_separator()
pixelmenu.add_command(label = "곱셈", command = multi)
pixelmenu.add_command(label = "나눗셈", command = div)
pixelmenu.add_separator()
pixelmenu.add_command(label = "감마", command = gamma)
pixelmenu.add_command(label = "이진화", command = binary)



geomenu = Menu(mainMenu)
mainMenu.add_cascade(label = '기하학 처리', menu = geomenu)
geomenu.add_command(label = '확대', command = zoomIn)
geomenu.add_command(label = '축소', command = zoomOut)
geomenu.add_separator()
geomenu.add_command(label = '상하반전', command = upDown)
geomenu.add_command(label = '좌우반전', command = leftRight)
geomenu.add_separator()
geomenu.add_command(label = '이동', command = move)
geomenu.add_command(label = '회전', command = rotate)
geomenu.add_separator()
geomenu.add_command(label = '겹쳐보기', command = overlap)


areaMenu = Menu(mainMenu)
mainMenu.add_cascade(label='영역처리', menu=areaMenu)
areaMenu.add_command(label='엠보싱', command=embossing)
areaMenu.add_separator()
areaMenu.add_command(label='블러링', command=blurr)
areaMenu.add_separator()
areaMenu.add_command(label='가우시안', command=gaussian)
areaMenu.add_separator()
areaMenu.add_command(label='샤프닝', command=Sharp)
areaMenu.add_separator()
areaMenu.add_command(label='경계선', command=Unsharp_Masking)

analyzeMenu = Menu(mainMenu);mainMenu.add_cascade(label='데이터분석', menu=analyzeMenu)
analyzeMenu.add_command(label='산술값', command=a_average)
analyzeMenu.add_command(label='히스토그램', command=a_histogram)
analyzeMenu.add_command(label='히스토그램(matplotlib)', command=a_histogram2)
analyzeMenu.add_separator()
analyzeMenu.add_command(label='히스토그램 스트래칭', command=a_histoStretch)
analyzeMenu.add_command(label='엔드-인 탐색', command=a_endInSearch)
analyzeMenu.add_command(label='히스토그램 평활화', command=a_histoEqual)



otherMenu = Menu(mainMenu);mainMenu.add_cascade(label='다른 포맷 처리', menu=otherMenu)
otherMenu.add_command(label='CSV로 내보내기', command=saveCSV)
otherMenu.add_command(label='CSV 불러오기', command=openCSV)
otherMenu.add_separator()
otherMenu.add_command(label='SQLite로 내보내기', command=saveSQLite)
otherMenu.add_command(label='SQLite에서 가져오기', command=openSQLite)
otherMenu.add_separator()
otherMenu.add_command(label='MySQL로 내보내기', command=saveMySQL)
otherMenu.add_command(label='MySQL에서 가져오기', command=openMySQL)
otherMenu.add_separator()
otherMenu.add_command(label='Excel로 내보내기(숫자)', command=saveExcel1)
otherMenu.add_command(label='Excel로 내보내기(음영)', command=saveExcel2)
window.mainloop()