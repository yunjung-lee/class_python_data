## 영상 처리 및 데이터 분석 툴

from tkinter import *; import os.path ;import math

from  tkinter.filedialog import *

from  tkinter.simpledialog import *

## 함수 선언부

def loadImage(fname) :

    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR,outImageG,outImageB , inW, inH, outW, outH




    photo = PhotoImage(file=filename)

    inW = photo.width();   inH = photo.height()




    inImageR, inImageG, inImageB  = [], [],[]; tmpList = []

    for i in range(inH) :  # 입력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(inW) :

            tmpList.append(0)

        inImageR.append(tmpList[:])

    for i in range(inH):  # 입력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(inW):

            tmpList.append(0)

        inImageG.append(tmpList[:])

    for i in range(inH):  # 입력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(inW):

            tmpList.append(0)

        inImageB.append(tmpList[:])




    # 파일 --> 메모리로 데이터 로딩

    for  i  in range(inH) :

        for  k  in  range(inW) :

            r, g, b = photo.get(k,i)

            #print(r,g,b,end='/')

            inImageR[i][k] = r

            inImageG[i][k] = g

            inImageB[i][k] = b

            #print(inImageR[i][k], inImageG[i][k], inImageB[i][k], end='/')

    photo=None




def openFile() :

    global window, canvas, paper, filename,inImageR, inImageG, inImageB, outImageR,outImageG,outImageB ,inW, inH, outW, outH

    filename = askopenfilename(parent=window,

                               filetypes=(("그림파일", "*.gif"), ("모든파일", "*.*")))

    loadImage(filename) # 파일 --> 입력메모리

    equal() # 입력메모리--> 출력메모리




def display() :

    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR,outImageG,outImageB, inW, inH, outW, outH

    # 기존에 캐버스 있으면 뜯어내기.

    if  canvas != None :

        canvas.destroy()

    # 화면 준비 (고정됨)

    window.geometry(str(outH) + 'x' + str(outW))

    canvas = Canvas(window, width=outW, height=outH)

    paper = PhotoImage(width=outW, height=outH)

    canvas.create_image((outW/2, outH/2), image=paper, state='normal')

    # 화면에 출력

    for i in range(outH) :

        for k in range(outW) :

            dataR = outImageR[i][k]

            dataG = outImageG[i][k]

            dataB = outImageB[i][k]

            #print(dataR, dataG, dataB, end='/')

            paper.put('#%02x%02x%02x' % (dataR, dataG, dataB), (k,i))

    canvas.pack()







def equal() :  # 동일 영상 알고리즘

    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR,outImageG,outImageB, inW, inH, outW, outH

    # 중요! 출력메모리의 크기를 결정

    outW = inW;  outH = inH;

    outImageR, outImageG, outImageB = [], [], [];   tmpList = []

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImageR.append(tmpList[:])

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)

        outImageG.append(tmpList[:])

    for i in range(outH):  # 출력메모리 확보(0으로 초기화)

        tmpList = []

        for k in range(outW):

            tmpList.append(0)