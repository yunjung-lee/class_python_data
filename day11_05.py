## 영상 처리 및 데이터 분석 툴
## 칼라이미지(R,G,B)


from tkinter import *; import os.path ;import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
import struct

## 함수 선언부

def loadImage(fname) :
    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR,outImageG,outImageB , inW, inH, outW, outH

    photo = PhotoImage(file=filename)

    inW = photo.width();   inH = photo.height()
    #빈 파일 생성
    inEmpty()

    # 파일 --> 메모리로 데이터 로딩
    for  i  in range(inH) :
        for  k  in  range(inW) :
            r, g, b = photo.get(k,i)
            inImageR[i][k] = r
            inImageG[i][k] = g
            inImageB[i][k] = b
    photo=None




def openFile() :

    global window, canvas, paper, filename,inImageR, inImageG, inImageB, outImageR,outImageG,outImageB ,inW, inH, outW, outH
    filename = askopenfilename(parent=window, filetypes=(("그림파일", "*.gif"), ("모든파일", "*.*")))

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
            paper.put('#%02x%02x%02x' % (dataR, dataG, dataB), (k,i))

    canvas.pack()


def inEmpty():
    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR, outImageG, outImageB, inW, inH, outW, outH

    inImageR, inImageG, inImageB = [], [], [];

    tmpList = []

    for i in range(inH):  # 입력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(inW):
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


def outEmpty():
    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR, outImageG, outImageB, inW, inH, outW, outH

    outImageR, outImageG, outImageB = [], [], [];
    tmpList = []

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
        outImageB.append(tmpList[:])


def equal() :  # 동일 영상 알고리즘

    global window, canvas, paper, filename, inImageR, inImageG, inImageB, outImageR,outImageG,outImageB, inW, inH, outW, outH

    # 중요! 출력메모리의 크기를 결정
    outW = inW;  outH = inH;

    #빈파일 생성
    outEmpty()
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            outImageR[i][k] = inImageR[i][k]
            outImageG[i][k] = inImageG[i][k]
            outImageB[i][k] = inImageB[i][k]
            # print(outImageR[i][k], outImageG[i][k], outImageB[i][k], end='/')
    display()




#

# def addImage() :  # 밝게하기 알고리즘

#     global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

#     # 중요! 출력메모리의 크기를 결정

#     outW = inW;  outH = inH;

#     outImage = [];   tmpList = []

#     for i in range(outH):  # 출력메모리 확보(0으로 초기화)

#         tmpList = []

#         for k in range(outW):

#             tmpList.append(0)

#         outImage.append(tmpList)

#     #############################

#     # 진짜 영상처리 알고리즘을 구현

#     ############################

#     value = askinteger('밝게하기', '밝게할 값-->', minvalue=1, maxvalue=255)

#     for  i  in  range(inH) :

#         for  k  in  range(inW) :

#             if inImage[i][k] + value > 255 :

#                 outImage[i][k] = 255

#             else :

#                 outImage[i][k] = inImage[i][k] + value

#     display()



def saveFile() :

    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH

    saveFp = asksaveasfile(parent=window, mode='w',defaultextension="*.gif", filetypes=(("그림파일", "*.gif"), ("모든파일", "*.*")))

    for i in range(outW):
        for k in range(outH):
            saveFp.write(struct.pack('B',str(outImageR[i][k])))
            saveFp.write(struct.pack('B', outImageG[i][k]))
            saveFp.write(struct.pack('B', outImageB[i][k]))

    saveFp.close()
    print('ok_save')




def exitFile() :

    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH

    pass




## 전역 변수부

window, canvas, paper, filename = [None] * 4

inImageR, inImageG, inImageB = [],[],[]

outImageR,outImageG,outImageB  = [],[],[]

inW, inH, outW, outH = [0] * 4




## 메인 코드부

window = Tk();  window.geometry('400x400');

window.title('GIF 영상 처리&데이터 분석 Ver 0.01')




mainMenu = Menu(window);window.config(menu=mainMenu)
fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu);mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)
#pixelMenu.add_command(label='밝게하기', command=addImage)


window.mainloop()