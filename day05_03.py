import rpy2
import nibabel as nib
import numpy as np
from tkinter import  *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import os.path
import math
import operator

#변수
fSize = 0
fName = 0
inH, inW,inD,outD, outW, outH,sx,sy,ex,ey = 0,0,0,0,0,0,0,0,0,0
inImageList,tmpList ,outImageList,rList,imgList,sliceList= [],[],[],[],[],[]
penYN = False
fileName ,window, canvas, paper= [None] * 4
# inW, inH, outW, outH = [0]*4                    #핵심변수
# penYN=False
# sx,sy,ex,ey =[0]*4

#함수
img =  nib.load("d:/dataset/IXI-T1/IXI002-Guys-0828-MPRAGESEN_-s256_-0301-00003-000001-01.nii")
print(img.shape)

def openfile():
    global inH, inW,inD,outD, outW, outH, sx, sy, ex, ey, penYN, inImageList,  outImageList,tmpList,rList,fileName, window, canvas, paper,img, imgList,sliceList
    imgList = np.arange(256*256*150).reshape(256,256,150)
    img = nib.load("d:/dataset/IXI-T1/IXI002-Guys-0828-MPRAGESEN_-s256_-0301-00003-000001-01.nii")
    imgList = np.load(img)
    sliceList=imgList[:,:,2]
    print(sliceList.shape)
    # fileName = askopenfilename(parent = window, filetype = (('RAW파일','*.raw'),('모든파일','*.*')))
    loadImage(fileName)
    equal()

def dummy_in():
    global inH, inW,inD,outD, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper,img, imgList,sliceList
    for i in range(inW):
        tmpList = []
        for k in range(inH):
            tmpList.append(0)
        rList.append(tmpList)

def dummy_out():
    global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper,img, imgList,sliceList
    rList=[]
    for i in range(outW):
        tmpList = []
        for k in range(outH):
            tmpList.append(0)
        rList.append(tmpList)

def loadImage(fName):
    global inH, inW, inD,outD,outW, outH, sx, sy, ex, ey, penYN,inImageList, outImageList,tmpList,rList,fileName, window, canvas, paper,img, imgList,sliceList
    fSize = os.path.getsize(fName)
    inH = inW = int(math.sqrt(fSize))
    inImageList = []
    dummy_in()
    inImageList=rList

    fp = open(fName, 'rb')
    print(fName)
    for i in range(inW):
        for k in range(inH):
            inImageList[i][k]=int(ord(fp.read(1)))                  # ord(fp.read(1))=?
    fp.close()

def equal():
    global inH, inW,inD,outD, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper,rList,img, imgList,sliceList
    outW=inW
    outH=inH
    dummy_out()
    outImageList = rList
    for i in range(inW):
        for k in range(inH):
            outImageList[i][k]=inImageList[i][k]
    display()

def display():
    global  inH, inW,inD,outD, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper,img, imgList,sliceList
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

# def bright():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     value = askinteger('밝게하기', '밝게 할 값 : ', minvalue = 1,maxvalue = 255)
#     for i in range(outW):
#         for k in range(outH):
#             if inImageList[i][k] + value >255:
#                 inImageList[i][k] = 255
#             else:
#                 outImageList[i][k]= inImageList[i][k] + value
#
#     display()
#
#
# def dark():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList,rList, fileName, window, canvas, paper
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     value = askinteger('어둡게하기', '어둡게 할 값 : ', minvalue = 1,maxvalue = 255)
#     for i in range(outW):
#         for k in range(outH):
#             if inImageList[i][k] + value <0 :
#                 inImageList[i][k] = 0
#             else:
#                 outImageList[i][k]= inImageList[i][k] - value
#
#     display()
#
# def revers():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     for i in range(outW):
#         for k in range(outH):
#             outImageList[i][k] = 255-inImageList[i][k]
#     display()
#
# def multi():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     value = askinteger('곱하기', '곱할 값 : ', minvalue=2, maxvalue=255)
#     for i in range(outW):
#         for k in range(outH):
#             if inImageList[i][k] + value > 255 :
#                 inImageList[i][k] = 255
#             else:
#                 outImageList[i][k] = inImageList[i][k]*value
#     display()
#
# def div():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     value = askinteger('나누기', '나눌 값 : ', minvalue=2, maxvalue=255)
#     for i in range(outW):
#         for k in range(outH):
#             outImageList[i][k] = int(inImageList[i][k]/value)
#     display()
#
# def gamma():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     value = askinteger('감마연산인자', '감마 상수(감마상수의 10배인 정수 : 2~10) : ', minvalue=2, maxvalue=10)
#     for i in range(outW):
#         for k in range(outH):
#             outImageList[i][k] = int(inImageList[i][k]**(value/10))
#     display()
#
# def zoomIn():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     value = askinteger('확대', '확대비율(2~16) : ', minvalue=2, maxvalue=10)
#     outW=inW*value
#     outH=inH*value
#     dummy_out()
#     outImageList=rList
#     for i in range(outW):
#         for k in range(outH):
#             outImageList[i][k]=inImageList[int(i/value)][int(k/value)]
#     display()
#
# def zoomOut():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     value = askinteger('축소', '축비율(2의 제곱수 : 2~16) : ', minvalue=2, maxvalue=16)
#     outW=int(inW/value)
#     outH=int(inH/value)
#     dummy_out()
#     outImageList=rList
#     for i in range(inW):
#         for k in range(inH):
#             outImageList[int(i / value)][int(k / value)] = inImageList[i][k]
#     display()
#
# def upDown():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     for i in range(inW):
#         for k in range(inH):
#             outImageList[outH-1-i][k] = inImageList[i][k]
#     display()
#
# def leftRight():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     for i in range(inW):
#         for k in range(inH):
#             outImageList[i][outH-1-k] = inImageList[i][k]
#     display()
#
# def move():
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     penYN = True
#
# def mouseClick(event):
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     if not penYN:
#         return
#     sx=event.x
#     sy=event.y
#
# def mouseMove(event):
#     global inH, inW, outW, outH, sx, sy, ex, ey, penYN, inImageList, outImageList, tmpList, rList, fileName, window, canvas, paper
#     if not penYN:
#         return
#     ex=event.x
#     ey=event.y
#     mx = ex - sx
#     my = ey - sy
#     outW=inW
#     outH=inH
#     dummy_out()
#     outImageList=rList
#     for i in range(inW):
#         for k in range(inH):
#             if 0< k-my < outH and 0< i-mx <outW:
#                 outImageList[i-mx][k-my] = inImageList[i][k]
#     penYN=False
#     display()


def exitfile():
    window.quit()
    window.destroy()


#메인

window = Tk()
window.geometry('800x600')
window.title('Image Ver.0.01 ')


mainMenu = Menu(window)
window.configure(menu = mainMenu)

filemenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = filemenu)
filemenu.add_command(label = '열기', command = openfile)
# # filemenu.add_separator()
# # filemenu.add_command(label = '저장', menu = savefile)
# # filemenu.add_separator()
# filemenu.add_command(label = '종료', command = exitfile)
#
# pixelmenu = Menu(mainMenu)
# mainMenu.add_cascade(label = '화소점 처리', menu = pixelmenu)
# pixelmenu.add_command(label = "밝게", command = bright)
# pixelmenu.add_separator()
# pixelmenu.add_command(label = "어둡게", command = dark)
# pixelmenu.add_separator()
# pixelmenu.add_command(label = "화소반전", command = revers)
# pixelmenu.add_separator()
# pixelmenu.add_command(label = "곱셈", command = multi)
# pixelmenu.add_separator()
# pixelmenu.add_command(label = "나눗셈", command = div)
# pixelmenu.add_separator()
# pixelmenu.add_command(label = "감마", command = gamma)
# pixelmenu.add_separator()
#
# geomenu = Menu(mainMenu)
# mainMenu.add_cascade(label = '기하학 처리', menu = geomenu)
# geomenu.add_command(label = '확대', command = zoomIn)
# geomenu.add_separator()
# geomenu.add_command(label = '축소', command = zoomOut)
# geomenu.add_separator()
# geomenu.add_command(label = '상하반전', command = upDown)
# geomenu.add_separator()
# geomenu.add_command(label = '좌우반전', command = leftRight)
# geomenu.add_separator()
# geomenu.add_command(label = '위치변경', command = move)
# geomenu.add_separator()

window.mainloop()
