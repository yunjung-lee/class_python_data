## 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리) ##

# 복습퀴즈1. GIF 영상 데이터 분석

# [파일]-[열기]에서  GIF 영상을 선택한 후에 다음의 내용이 윈도창의 Label에 출력되도록 한다.

# 최소/최다 출현 r픽셀값: (138, 1) (189, 1612)

# 최소/최다 출현 g픽셀값: (137, 1) (209, 1298)

# 최소/최다 출현 b픽셀값: (10, 1) (99, 2531)

# r,g,b픽셀 평균값: 194.80955 159.2699 109.461

# r,g,b픽셀 중위수: 196 157 91


from tkinter import *
import os.path
import math
from tkinter.filedialog import *
import operator

# 변수
filename ='d:/data_analysis'

# 함수
def openFile():
    global photo
    filename = askopenfilename(parent=window, filetypes=(('GIF파일', '*.gif'), ('모든파일', '*.*')))
    photo = PhotoImage(file = filename)
    label1.configure(image = photo)
    label1.image = photo


def pixleFile():
    global photo
    rDic,gDic,bDic = {},{},{}                          #색상: 개수 딕셔너리
    xSize = photo.width()
    ySixz = photo.height()
    for i in range(xSize):
        for k in range(ySixz):
            r,g,b = photo.get(i,k)
            if r in rDic:
                rDic[r] += 1
            else:
                rDic[r] = 1
    for i in range(xSize):
        for k in range(ySixz):
            r, g, b = photo.get(i, k)

            if g in gDic:
                gDic[g] += 1
            else:
                gDic[g] = 1
    for i in range(xSize):
        for k in range(ySixz):
            r, g, b = photo.get(i, k)
            if b in bDic:
                bDic[b] += 1
            else:
                bDic[b] = 1
    countListR = sorted(rDic.items(),key=operator.itemgetter(1))
    countListG = sorted(gDic.items(),key=operator.itemgetter(1))
    countListB = sorted(bDic.items(),key=operator.itemgetter(1))
    print('최소출현 r필셀값',countListR[0],'최다출현 r필셀값', countListR[-1])
    print('최소출현 g필셀값',countListG[0],'최다출현 g필셀값', countListG[-1])
    print('최소출현 b필셀값',countListB[0],'최다출현 b필셀값', countListB[-1])

def mathFile():
    global photo
    rSum,gSum,bSum = [0]*3
    rDic,gDic,bDic = {},{},{}                          #색상: 개수 딕셔너리
    xSize = photo.width()
    ySixz = photo.height()
    for i in range(xSize):
        for k in range(ySixz):
            r,g,b = photo.get(i,k)
            if r in rDic:
                rDic[r] += 1
            else:
                rDic[r] = 1
    for i in range(xSize):
        for k in range(ySixz):
            r, g, b = photo.get(i, k)

            if g in gDic:
                gDic[g] += 1
            else:
                gDic[g] = 1
    for i in range(xSize):
        for k in range(ySixz):
            r, g, b = photo.get(i, k)
            if b in bDic:
                bDic[b] += 1
            else:
                bDic[b] = 1
    countListR = sorted(rDic.items(),key=operator.itemgetter(1))
    countListG = sorted(gDic.items(),key=operator.itemgetter(1))
    countListB = sorted(bDic.items(),key=operator.itemgetter(1))

    for item in countListR:
        rSum += item[0]*item[1]
    rAvg = rSum/(xSize*ySixz)

    for item in countListG:
        gSum += item[0]*item[1]
    gAvg = gSum/(xSize*ySixz)

    for item in countListB:
        bSum += item[0]*item[1]
    bAvg = bSum/(xSize*ySixz)
    print('r,g,b픽셀 평균값:' +str(rAvg)+','+str(gAvg) +','+str(bAvg))

    rStream, gStream, bStream = [],[],[]
    meadia = int((xSize*ySixz)/2)
    for item in countListR:
        for i in range(item[1]):
            rStream.append(item[0])

    for item in countListG:
        for i in range(item[1]):
            gStream.append(item[0])

    for item in countListB:
        for i in range(item[1]):
            bStream.append(item[0])

    print('r,g,b픽셀 중위수:' + str(rStream[meadia])+','+str(gStream[meadia])+','+str(bStream[meadia]))



# 메인코드
window = Tk()
window.geometry('400x400')

photo = PhotoImage()
label1 = Label(window, image = photo)
label1.pack()

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '열기',command = openFile)
fileMenu.add_separator()
fileMenu.add_command(label = 'pixel',command = pixleFile)
fileMenu.add_separator()
fileMenu.add_command(label = 'mean,median',command = mathFile)

window.mainloop()


# 복습퀴즈3(선택). p325. 그림판 만들기

