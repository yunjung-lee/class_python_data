## 영상 처리 및 데이터 분석 툴

## 1. 영상 밝게하기 처리 전에, 64x64 크기로 결과를 미리보기하는 기능 추가
## 2. Lookup Table을 활용한 파라볼라 기능 추가


from tkinter import *; import os.path ;import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
import math
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



def  an_average() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 입력 영상 평균값 계산하기
    rawDic = {}  # 픽셀 카운트
    for  i  in  range(inW) :
        for  k  in  range(inH) :
            value = inImage[i][k]
            if  value  in  rawDic :
                rawDic[value] += 1
            else :
                rawDic[value] = 1
    rawSum = 0
    rawKeyList = list(rawDic.keys())
    for value in rawKeyList:
        rawSum += value * rawDic[value]
    inRawAvg = rawSum / (inW * inH)

    # 출력 영상 평균값 계산하기
    rawDic = {}  # 픽셀 카운트
    for i in range(outW):
        for k in range(outH):
            value = outImage[i][k]
            if value in rawDic:
                rawDic[value] += 1
            else:
                rawDic[value] = 1
    rawSum = 0
    rawKeyList = list(rawDic.keys())
    for value in rawKeyList:
        rawSum += value * rawDic[value]
    outRawAvg = rawSum / (outW * outH)

    subWindow = Toplevel(window)
    subWindow.geometry('200x100')
    label1= Label(subWindow, text='입력영상 평균 -->' + str(math.floor(inRawAvg)));    label1.pack()
    label2 = Label(subWindow, text='출력영상 평균 -->' + str(math.floor(outRawAvg)));   label2.pack()
    subWindow.mainloop()



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

def paraCap() :  # 파라볼라 캡.
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    Lookup = [0] * 256
    for i in range(256) :
        Lookup[i] = int(255- 255.0 * (( i / 128.0 - 1) * ( i / 128.0 - 1)))

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
                outImage[i][k] = Lookup[inImage[i][k]]

    display()



def pre_addImage() :  # 64x64 크기의 [밝게하기 프리뷰]
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # 중요! 출력메모리의 크기를 결정
    p_outW = 64;  p_outH = 64;
    p_outImage = [];   tmpList = []
    for i in range(p_outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(p_outW):
            tmpList.append(0)
        p_outImage.append(tmpList)
    #############################
    # 진짜 영상처리 알고리즘을 구현
    ############################
    step = int(inW/p_outW)
    value = askinteger('(Preview)밝게하기', '밝게할 값-->', minvalue=1, maxvalue=255)
    for  i  in  range(0,inH,step) :
        for  k  in  range(0,inH,step) :
            if inImage[i][k] + value > 255 :
                p_outImage[int(i/step)][int(k/step)] = 255
            else :
                p_outImage[int(i/step)][int(k/step)] = inImage[i][k] + value
    displayPreview(p_outImage, p_outW, p_outH)

def displayPreview(poImage, poW, poH ) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    subWindow = Toplevel(window)
    subWindow.geometry(str(poH) + 'x' + str(poW))
    subcanvas = Canvas(subWindow, width=poW, height=poH)
    subpaper = PhotoImage(width=poW, height=poH)
    subcanvas.create_image((poW/2, poH/2), image=subpaper, state='normal')
    # 화면에 출력
    for i in range(poH) :
        for k in range(poW) :
            data = poImage[i][k]
            print(data, end=' ')
            subpaper.put('#%02x%02x%02x' % (data, data, data), (k,i))
    subcanvas.pack()
    subWindow.mainloop()

def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

def exitFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

## 전역 변수부
window, canvas, paper, filename = [None] * 4
inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4

## 메인 코드부
window = Tk();  window.geometry('400x400');
window.title('영상 처리&데이터 분석')

mainMenu = Menu(window);window.config(menu=mainMenu)
fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu);mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)
pixelMenu.add_command(label='밝게하기', command=addImage)
pixelMenu.add_command(label='파라볼라-캡(Lookup)', command=paraCap)


analyzeMenu = Menu(mainMenu);mainMenu.add_cascade(label='데이터 분석', menu=analyzeMenu)
analyzeMenu.add_command(label='평균값', command=an_average)

previewMenu = Menu(mainMenu);mainMenu.add_cascade(label='미리보기', menu=previewMenu)
previewMenu.add_command(label='밝게하기', command=pre_addImage)



window.mainloop()