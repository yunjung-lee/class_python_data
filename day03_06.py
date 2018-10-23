#GIF 이미지 뷰어&데이터 분석###

from tkinter import  *
from tkinter.filedialog import *
import operator



#함수 선언부

def openFile():
    global photo
    filename = askopenfilename(parent = window, filetypes = (('GIF파일','*.gif'),('모든파일','*.*')))
 #위의 경로의 파일을 보이기 함
    photo = PhotoImage(file = filename)             #3줄은 구문처럼 외우기
    pLabel1.configure(image = photo)
    pLabel1.image = photo

def analyzeGIF():
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

#평균 구하기
    rSum = 0
    for item in rDic:
        rSum += item[0]*item[1]
    rAvg = rSum/(xSize*ySixz)


def exitFile():
    window.quit()
    window.destroy()                                #안에 있는 자료까지 없애는 구문(모두 없애야 한다.항상 두개를 같이)
#전역 변수부
photo=None

##메인 코드부
window = Tk()
window.geometry('400x400')

photo = PhotoImage()
pLabel1 = Label(window, image = photo)
pLabel1.pack(expand = 1, anchor = CENTER)                   # 빈 사진 위치 준비

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '열기(Ctrl+o)',command = openFile)
fileMenu.add_separator()
fileMenu.add_command(label = ' GIF 데이터 분석',command = analyzeGIF)
fileMenu.add_separator()
fileMenu.add_command(label = '종료(Ctrl+x)',command = exitFile)


window.mainloop()