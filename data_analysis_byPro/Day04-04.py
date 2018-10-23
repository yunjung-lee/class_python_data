## 영상 처리 및 데이터 분석 툴
from tkinter import *; import os.path ;import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
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
    for i in range(outH) :
        for k in range(outW) :
            data = outImage[i][k]
            paper.put('#%02x%02x%02x' % (data, data, data), (k,i))
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


def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

def exitFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

## 전역 변수부
window, canvas, paper, filename = [None] * 4
inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4
panYN = False;  sx, sy, ex, ey = [0] * 4

## 메인 코드부
window = Tk();  window.geometry('200x200');
window.title('영상 처리&데이터 분석 Ver 0.2')
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


analyzeMenu = Menu(mainMenu);mainMenu.add_cascade(label='데이터분석', menu=analyzeMenu)
analyzeMenu.add_command(label='평균값', command=a_average)

window.mainloop()