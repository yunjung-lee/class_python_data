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

# def binary():
#     global penYN1, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     penYN1=True
#     print(sx,sy)
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     value = inImageList[sx][sy]
#     for i in range(outW):
#         for k in range(outH):
#             if inImageList[i][k]>value:
#                 outImageList[i][k] = 255
#             else:
#                 outImageList[i][k] = 0
#
#     print(sx, sy)
#
# def mouseClick(event1):
#     global penYN1, inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     if not penYN1:
#         return
#     sx=event1.x
#     sy=event1.y


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



def exitfile():
    window.quit()
    window.destroy()


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
pixelmenu.add_separator()
pixelmenu.add_command(label = "어둡게", command = dark)
pixelmenu.add_separator()
pixelmenu.add_command(label = "화소반전", command = revers)
pixelmenu.add_separator()
pixelmenu.add_command(label = "곱셈", command = multi)
pixelmenu.add_separator()
pixelmenu.add_command(label = "나눗셈", command = div)
pixelmenu.add_separator()
pixelmenu.add_command(label = "감마", command = gamma)
pixelmenu.add_separator()
pixelmenu.add_command(label = "이진화", command = binary)
pixelmenu.add_separator()
# pixelmenu.add_command(label = "클릭 위치 저장", command = mc)
# pixelmenu.add_separator()


geomenu = Menu(mainMenu)
mainMenu.add_cascade(label = '기하학 처리', menu = geomenu)
geomenu.add_command(label = '확대', command = zoomIn)
geomenu.add_separator()
geomenu.add_command(label = '축소', command = zoomOut)
geomenu.add_separator()
geomenu.add_command(label = '상하반전', command = upDown)
geomenu.add_separator()
geomenu.add_command(label = '좌우반전', command = leftRight)
geomenu.add_separator()
geomenu.add_command(label = '위치변경', command = move)
geomenu.add_separator()
geomenu.add_command(label = '회전', command = rotate)
geomenu.add_separator()
geomenu.add_command(label = '영상 합성', command = overlap)
geomenu.add_separator()

window.mainloop()