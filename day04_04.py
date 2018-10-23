##정방형 raw이미지 처리
##그레이 스케일: 밝기만 표현(0:블랙,255: 화이트)
##밝게 : 숫자를 더함,어둡게 : 숫자를 뺌

from  tkinter import *
import os.path
import math
from tkinter.filedialog import *
from tkinter.simpledialog import *
import operator

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



def openFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    filename = askopenfilename(parent = window, filetypes = (('RAW파일','*.raw'),('모든파일','*.*')))
 #위의 경로의 파일을 보이기 함
    loadImage(filename)             # 파일에서 --> 입력 메모리
    euqal()                            # 파일에서 --> 출력 메모리

def display():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    #기존의 캔버스 있ㅇ드면 뜯어내기
    if canvas != None:
        canvas.destroy()

    #화면 준비(고정)
    window.geometry(str(outH)+'x'+str(outW))
    canvas = Canvas(window, width=outW,height = outH)

    paper =  PhotoImage(width=outW,height = outH)

    canvas.create_image((outW/2,outH/2),image = (paper), state = 'normal')

    #화면 출력
    for i in range(outH):
        for k in range(outW):
            data =  outImage[i][k]
            paper.put('#%02x%02x%02x' % (data,data,data), (k,i))  # r,g,b,때문에 data*3


    canvas.pack()

def euqal():                          #동일 영상 알고르즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
# 중요!! 출력 메모리의 크기 결정
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)        # 램에 0으로 영역 확보
    #######################################
    # 진짜 영상 처리 알고리즘 구현 ####
    ######################################
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = inImage[i][k]                  # 확보된 영역에 진짜 이미지 삽입
    display()

def addImage():                          #밝게 하기 알고르즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
# 중요!! 출력 메모리의 크기 결정
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)        # 램에 0으로 영역 확보
    #######################################
    # 진짜 영상 처리 알고리즘 구현 ####
    ######################################
    value = askinteger('밝게하기', '밝게 할 값 ==>', minvalue=1, maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] + value>255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = inImage[i][k] + value               # 확보된 영역에 진짜 이미지 삽입
    display()

def darkFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)        # 램에 0으로 영역 확보
    #######################################
    # 진짜 영상 처리 알고리즘 구현 ####
    ######################################
    value = askinteger('어둡게하기', '어둡게 할 값 ==>', minvalue=1, maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] - value<0:
                outImage[i][k] = 0
            else:
                outImage[i][k] = inImage[i][k] - value               # 확보된 영역에 진짜 이미지 삽입
    display()

def xFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)        # 램에 0으로 영역 확보
    #######################################
    # 진짜 영상 처리 알고리즘 구현 ####
    ######################################
    value = askinteger('밝게 할 비율',  '밝게 할 비율값 ==>', minvalue=1, maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            if inImage[i][k] * value>255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = inImage[i][k] * value
    display()

def yFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)        # 램에 0으로 영역 확보
    #######################################
    # 진짜 영상 처리 알고리즘 구현 ####
    ######################################
    value = askinteger('어둡게 할 비율',  '어둡게 할 비율값 ==>', minvalue=1, maxvalue=255)
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = inImage[i][k] / value
    display()

def transformFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    for i in range(inH):
        for k in range(inW):
            outImage[i][k] = 255-inImage[i][k]                # 확보된 영역에 진짜 이미지 삽입
    display()


def Gamma():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)        # 램에 0으로 영역 확보
    #######################################
    # 진짜 영상 처리 알고리즘 구현 ####
    ######################################
    value = askinteger('gamma*10',  'gamma(1~20) ==>', minvalue=1, maxvalue=20)
    for i in range(inH):
        for k in range(inW):
            if int(inImage[i][k] **(value/10))>255:
                outImage[i][k] = 255
            else:
                outImage[i][k] = int(inImage[i][k] **(value/10))
    display()


def a_average():                #입출력 영상의 평균값
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    rawSum = 0
    for i in range(inH):
        for k in  range(inW):
            rawSum += inImage[i][k]
    inRawAvg = int(rawSum/(inH*inW))

    rawSum = 0
    for i in range(outH):
        for k in  range(outW):
            rawSum += outImage[i][k]
    outRawAvg = int(rawSum/(outH*outW))

    subwindow = Toplevel(window)                #부모(window)에 종속된 서브윈도우
    subwindow.geometry('200x100')
    label1=Label(subwindow, text = 'k입력 영상 평균값-->'+str(inRawAvg))
    label1.pack()
    label2 = Label(subwindow, text='k입력 영상 평균값-->' + str(outRawAvg))
    label2.pack()

def minMax():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    # rawSum = 0
    # outDic={}
    # for i in range(inH):
    #     for k in  range(inW):
    #         r = inImage.get(i,k)
    #         if r in outDic:
    #             outDic[r] += 1
    #         else:
    #             outDic[r] = 1
    # print(outDic)
    #
    # countListR = sorted(outDic.items(),key=operator.itemgetter(1))
    # print('최소출현 필셀값', countListR[0], '최다출현 필셀값', countListR[-1])


def upDown():                          #동일 영상 알고르즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    for i in range(inH):
        for k in range(inW):
            outImage[outW-1-i][k] = inImage[i][k]                  # 확보된 영역에 진짜 이미지 삽입
    display()

def panImage():                          #동일 영상 알고르즘
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, penYN
    penYN = True

def mouseClick(event):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH,sx,sy,ex,ey,penYN
    if not penYN:
        return
    sx = event.x
    sy = event.y

def mouseDrop(event):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH, sx, sy, ex, ey, penYN
    if not penYN:
        return
    ex = event.x
    ey = event.y
    mx = sx-ex
    my = sy-ey
    outW = inW
    outH = inH
    outImage=[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImage.append(tmpList)
    for i in range(inH):
        for k in range(inW):
            if 0<= i-mx<outH and 0<k-my<outW:
                outImage[i-mx][k-my] = inImage[i][k]
    penYN = False
    display()

def cancelFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass

def exitFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass


def saveFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass



#전역 변수부
window, canvas, paper,filename = [None]*4
inImage, outImage =[],[]                        #부가변수
inW, inH, outW, outH = [0]*4                    #핵심변수
penYN=False
sx,sy,ex,ey =[0]*4

#메인 코드부
window = Tk()
window.geometry('400x400')
window.title('영상처리 & 데이터분석 Ver 0.08')
window.bind('<Button-1>',mouseClick)
window.bind('<ButtonRelease-1>',mouseDrop)

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '열기',command = openFile)
fileMenu.add_separator()
fileMenu.add_command(label = '저장',command = saveFile)
fileMenu.add_separator()
fileMenu.add_command(label = '종료',command = exitFile)
# fileMenu.add_separator()
# fileMenu.add_command(label = '인쇄',command = printFile)
# fileMenu.add_separator()
# fileMenu.add_command(label = '명령 취소',command = cancelFile)

pixelMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '화소점처리', menu = pixelMenu)
pixelMenu.add_command(label = '동일영상',command =  euqal )
pixelMenu.add_separator()
pixelMenu.add_command(label = '밝게 하기',command = addImage)
pixelMenu.add_separator()
pixelMenu.add_command(label = '어둡게 하기',command = darkFile)
pixelMenu.add_separator()
pixelMenu.add_command(label = '곱셈',command = xFile)
pixelMenu.add_separator()
pixelMenu.add_command(label = '나눗셈',command = yFile)
pixelMenu.add_separator()
pixelMenu.add_command(label = '화소 반전',command = transformFile)
pixelMenu.add_separator()
pixelMenu.add_command(label = '감마',command = Gamma)
# pixelMenu.add_separator()
# pixelMenu.add_command(label = '파라볼라',command = parabolaCap)
# pixelMenu.add_separator()
# pixelMenu.add_command(label = '파라볼라',command = parabolaCup )
#
#
# layoutMenu = Menu(mainMenu)
# mainMenu.add_cascade(label = '레이아웃', menu = layoutMenu)
# layoutMenu.add_command(label = '레이아웃 추가',command = newLayoutFile )
# layoutMenu.add_separator()
# layoutMenu.add_command(label = '레이아웃 삭제',command = deletLayoutFile)
# layoutMenu.add_separator()
# layoutMenu.add_command(label = '레이아웃 겹쳐보기',command = overlapLayoutFile)
#
analyzeMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '데이터 분석', menu = analyzeMenu)
analyzeMenu.add_command(label = '평균',command =  a_average)
analyzeMenu.add_separator()
analyzeMenu.add_command(label = '최대값&최소값',command = minMax)
# analyzeMenu.add_separator()
# analyzeMenu.add_command(label = '영역선택',command = areaFile)
# analyzeMenu.add_separator()
# analyzeMenu.add_command(label = '영역정보',command = areaInfoFile)
# analyzeMenu.add_separator()
# analyzeMenu.add_command(label = 'integration',command = integrationFile)

geoMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '기하학 처리', menu = geoMenu)
geoMenu.add_command(label = '상하반전',command =  upDown)
geoMenu.add_separator()
geoMenu.add_command(label = '이동',command = panImage)

# 영상처리를 위한 알고리즘이 어떤 것이 있는지 알아보고 메뉴에 추가해 놓기 15개


window.mainloop()
