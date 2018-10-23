##정방형 raw이미지 처리
##그레이 스케일: 밝기만 표현(0:블랙,255: 화이트)
##밝게 : 숫자를 더함,어둡게 : 숫자를 뺌

from  tkinter import *
import os.path
import math

##영상 처리 및 데이터 분석 툴


#함수 선언부
def loadImage(fname):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    fsize = os.path.getsize(fname)                                               #파일 크기 확인
    inH=inW=int(math.sqrt(fsize))                                           #중요!!:입력 메모리 크기 결정!! 미리 이미지가 들어올 공간 확보(루트를 쓰려고 정방으로 이미지 변경)
    inImage=[]
    for i in range(inH):
        tmpList =[]
        for k in range(inW):                                                #입력 메모리 확보(0으로 초기화)
            tmpList.append(0)
        inImage.append(tmpList)
    #파일에서 메모리로 데이터 로딩
    fp = open(fname,'rb')                                   #파일에서 열기(바이너리 모드)
    for i in range(inH):
        for k in range(inW):
            inImage[i][k] = int(ord(fp.read(1)))
    fp.close()

    print(inImage[100][100])


def openFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    filename = 'D:\image\image1.raw'
    loadImage(filename)
    pass

def saveFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass

def exitFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass


def brightFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass

def darkFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass

def reversFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass



#전역 변수부
window, canvas, paper,filename = [None]*4
inImage, outImage =[],[]                        #부가변수
inW, inH, outW, outH = [0]*4                    #핵심변수

#메인 코드부
window = Tk()
window.geometry('400x400')
window.title('영상처리 & 데이터분석 Ver 0.01')

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '열기',command = openFile)
fileMenu.add_separator()
fileMenu.add_command(label = '저장',command = saveFile)
fileMenu.add_separator()
fileMenu.add_command(label = '종료',command = exitFile)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '영상처리', menu = editMenu)
editMenu.add_command(label = '밝게하기',command = brightFile )
editMenu.add_separator()
editMenu.add_command(label = '어둡게하기',command = darkFile)
editMenu.add_separator()
editMenu.add_command(label = '반전하기',command = reversFile)

# 영상처리를 위한 알고리즘이 어떤 것이 있는지 알아보고 메뉴에 추가해 놓기 15개


window.mainloop()























