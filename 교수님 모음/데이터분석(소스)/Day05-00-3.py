## 영상 처리 및 데이터 분석 툴

## (1) 파일 저장 추가
## (2) 스레드를 활용한 디스플레이 처리.... display() 함수만 변경됨.  --> 성능 향상 없음.


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


import threading
import queue

def display() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, paper1, paper2, paper3, paper4
    # 기존에 캐버스 있으면 뜯어내기.
    if  canvas != None :
        canvas.destroy()
    # 화면 준비 (고정됨)
    window.geometry(str(outH) + 'x' + str(outW))
    canvas = Canvas(window, width=outW, height=outH)
    paper1 = PhotoImage(width=int(outW/2), height=int(outH/2))
    paper2 = PhotoImage(width=int(outW/2), height=int(outH/2))
    paper3 = PhotoImage(width=int(outW/2), height=int(outH/2))
    paper4 = PhotoImage(width=int(outW/2), height=int(outH/2))
    canvas.create_image((outW / 2 - outW / 4, outH / 2 - outH / 4), image=paper1, state='normal')
    canvas.create_image((outW / 2 - outW / 4, outH / 2 + outH / 4), image=paper2, state='normal')
    canvas.create_image((outW / 2 + outW / 4, outH / 2 - outH / 4), image=paper4, state='normal')
    canvas.create_image((outW / 2 + outW / 4, outH / 2 + outH / 4), image=paper3, state='normal')
    # 화면에 출력
    def putPixel1() :
        for i in range(0, int(outH/2)) :
            for k in range(0, int(outW/2)) :
                data = outImage[i][k]
                paper1.put('#%02x%02x%02x' % (data, data, data), (k,i))

    def putPixel2() :
        for i in range(int(outH/2), outH) :
            for k in range(0, int(outW/2)) :
                data = outImage[i][k]
                paper2.put('#%02x%02x%02x' % (data, data, data), (k,i-int(outH/2)))


    def putPixel3() :
        for i in range(int(outH/2),outH) :
            for k in range(int(outW/2),outW) :
                data = outImage[i][k]
                paper3.put('#%02x%02x%02x' % (data, data, data), (k-int(outW/2),i-int(outH/2)))

    def putPixel4():
        for i in range(0, outH):
            for k in range(int(outW / 2), outW):
                data = outImage[i][k]
                paper4.put('#%02x%02x%02x' % (data, data, data), (k-int(outW / 2), i))

    canvas.pack()

    threading.Thread(target=putPixel1).start()
    threading.Thread(target=putPixel2).start()
    threading.Thread(target=putPixel3).start()
    threading.Thread(target=putPixel4).start()


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




import struct
def saveFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.raw", filetypes=(("RAW파일", "*.raw"), ("모든파일", "*.*")))
    for i in range(outW):
        for k in range(outH):
            saveFp.write( struct.pack('B',outImage[i][k]))

    saveFp.close()

def exitFile() :
    global window, canvas, paper, filename,inImage, outImage,inW, inH, outW, outH
    pass

## 전역 변수부
window, canvas, paper, filename = [None] * 4
paper1, paper2, paper3, paper4 = [None] * 4
inImage, outImage = [], []; inW, inH, outW, outH = [0] * 4

## 메인 코드부
window = Tk();  window.geometry('400x400');
window.title('영상 처리&데이터 분석 Ver 0.3')

mainMenu = Menu(window);window.config(menu=mainMenu)
fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=openFile)
fileMenu.add_command(label='저장', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=exitFile)

pixelMenu = Menu(mainMenu);mainMenu.add_cascade(label='화소점처리', menu=pixelMenu)
pixelMenu.add_command(label='동일영상', command=equal)
pixelMenu.add_command(label='밝게하기',  command=addImage)





window.mainloop()