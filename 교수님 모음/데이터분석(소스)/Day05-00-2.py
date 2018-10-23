## 영상 처리 및 데이터 분석 툴

## (1) 대용량 영상을 128x128로 미리보기
## 데이터 처리는 그대로이며 display() 함수에서만 128x128로....
## (2) 스레드로 디스플레이
## (3) 상태바에 파일명과 크기를 명시


from tkinter import *; import os.path ;import math
from  tkinter.filedialog import *
from  tkinter.simpledialog import *
import math
## 함수 선언부
def loadImage(fname) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, status
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
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH, status
    filename = askopenfilename(parent=window,
                               filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    inImage.clear(); outImage.clear()
    loadImage(filename) # 파일 --> 입력메모리
    equal() # 입력메모리--> 출력메모리

    # 상태바에 파일 정보 출력
    statusStr = '파일명:' + filename + "\n파일크기:" + str(inW) + "x"  + str(inH)
    status.configure(text=statusStr)

import threading
def display() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, VIEW_X, VIEW_Y

    # 출력할 영상에서 STEP을 구한다.
    VIEW_X, VIEW_Y = 128, 128
    if VIEW_X > outW or VIEW_Y > outH : #결과 영상이 128 미만이면
        VIEW_X = outW; VIEW_Y = outH
        step = 1
    else :
        step = int(outW / VIEW_X)
    print(outW, VIEW_X, step)
    # 기존에 캐버스 있으면 뜯어내기.
    if  canvas != None :
        canvas.destroy()
    # 화면 준비 (고정됨)
    window.geometry(str(VIEW_X*2) + 'x' + str(VIEW_Y*2))
    canvas = Canvas(window, width=VIEW_X, height=VIEW_Y)
    paper = PhotoImage(width=VIEW_X, height=VIEW_Y)
    canvas.create_image((VIEW_X/2, VIEW_Y/2), image=paper, state='normal')

    # 화면에 출력
    def putPixel():
        for i in range(0,outH, step) :
            for k in range(0,outW, step) :
                data = outImage[i][k]
                paper.put('#%02x%02x%02x' % (data, data, data), (int(k/step),int(i/step)))

    threading.Thread(target=putPixel).start()
    canvas.pack(expand=1, anchor=CENTER)


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



def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

def exitFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

## 전역 변수부
window, canvas, paper, filename = [None] * 4
inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4
VIEW_X, VIEW_Y = 128, 128 # 디스플레이 크기 고정
status=None
## 메인 코드부
window = Tk();  window.geometry('400x400');
window.title('영상 처리&데이터 분석')

status = Label(window, text="이미지 정보", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


mainMenu = Menu(window);window.config(menu=mainMenu)
fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu);mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)
pixelMenu.add_command(label='밝게하기', command=addImage)


window.mainloop()