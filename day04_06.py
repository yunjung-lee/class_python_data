##정방형 raw이미지 처리
##그레이 스케일: 밝기만 표현(0:블랙,255: 화이트)
##밝게 : 숫자를 더함,어둡게 : 숫자를 뺌

from  tkinter import *
import os.path
import math
from tkinter.filedialog import *
from tkinter.simpledialog import *

##영상 처리 및 데이터 분석 툴


#함수 선언부
def loadImage(fname):
    global window, canvas, paper, filename, inImageR,inImageG, inImageB, outImageR,outImageG, outImageB, inW, inH, outW, outH

    photo = PhotoImage(file=filename)               #gif는 fsize가 이미지 사이즈와 동일하지 않다.fileopen 개념임
    inW = photo.width()
    inH = photo.height()

    inImageR, inImageG, inImageB =[],[],[]


    for i in range(inH):
        tmpList =[]
        for k in range(inW):                                                #입력 메모리 확보(0으로 초기화)
            tmpList.append(0)
        inImageR.append(tmpList[:])
        inImageG.append(tmpList[:])
        inImageB.append(tmpList[:])
    #파일에서 메모리로 데이터 로딩

    for i in range(inH):
        for k in range(inW):
            r,g,b = photo.get(i,k)
            inImageR[i][k] =r
            inImageG[i][k] =g
            inImageB[i][k] =b

    photo = None                                        #큰 메모리 사용을 비워서 가벼워지는 효과




def openFile():
    global window, canvas, paper,filename,inImageR,inImageG, inImageB, outImageR,outImageG, outImageB,inW, inH, outW, outH
    filename = askopenfilename(parent = window, filetypes = (('GIF파일','*.gif'),('모든파일','*.*')))
 #위의 경로의 파일을 보이기 함
    loadImage(filename)             # 파일에서 --> 입력 메모리
    euqal()                            # 파일에서 --> 출력 메모리

def display():
    global window, canvas, paper, filename, inImageR,inImageG, inImageB, outImageR,outImageG, outImageB, inW, inH, outW, outH,dataR,dataG,dataB
    #기존의 캔버스 있ㅇ드면 뜯어내기
    if canvas != None:
        canvas.destroy()

    #화면 준비(고정)
    window.geometry(str(outH)+'x'+str(outW))
    canvas = Canvas(window, width=outW,height = outH)
    canvas2 = Canvas(window, width=outW, height=outH)
    paper =  PhotoImage(width=outW,height = outH)
    paper2 = PhotoImage(width=outW, height=outH)
    canvas.create_image((outW/2,outH/2),image = (paper), state = 'normal')
    canvas.create_image((outW / 2, outH / 2), image=(paper2), state='normal')
    #화면 출력
    for i in range(outH):
        for k in range(outW):
            dataR = outImageR[i][k]
            dataG = outImageG[i][k]
            dataB = outImageB[i][k]
            paper.put('#%02x%02x%02x' % (dataR,dataG,dataB), (i,k))  # r,g,b,때문에 data*3
    for i in range(inH):
        for k in range(inW):
            dataR = inImageG[i][k]
            dataG = inImageB[i][k]
            dataB = inImageR[i][k]
            paper2.put('#%02x%02x%02x' % (dataR,dataG,dataB), (i,k))  # r,g,b,때문에 data*3

    canvas.pack()

def euqal():                          #동일 영상 알고르즘
    global window, canvas, paper, filename, inImageR,inImageG, inImageB, outImageR,outImageG, outImageB, inW, inH, outW, outH
# 중요!! 출력 메모리의 크기 결정
    outW = inW
    outH = inH
    outImageR, outImageG, outImageB=[],[],[]
    tmpList = []
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageR.append(tmpList[:])        # 램에 0으로 영역 확보
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageG.append(tmpList[:])
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageB.append(tmpList[:])
    #######################################
    # 진짜 영상 처리 알고리즘 구현 ####
    ######################################
    for i in range(inH):
        for k in range(inW):
            outImageR[i][k] = inImageR[i][k]                  # 확보된 영역에 진짜 이미지 삽입
            outImageG[i][k] = inImageG[i][k]
            outImageB[i][k] = inImageB[i][k]
    display()

# def addImage():                          #밝게 하기 알고르즘
#     global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
# # 중요!! 출력 메모리의 크기 결정
#     outW = inW
#     outH = inH
#     outImage=[]
#     tmpList = []
#     for i in range(outH):
#         tmpList = []
#         for k in range(outW):
#             tmpList.append(0)
#         outImage.append(tmpList)        # 램에 0으로 영역 확보
#     #######################################
#     # 진짜 영상 처리 알고리즘 구현 ####
#     ######################################
#     value = askinteger('밝게하기', '밝게 할 값 ==>', minvalue=1, maxvalue=255)
#     for i in range(inH):
#         for k in range(inW):
#             if inImage[i][k] + value>255:
#                 outImage[i][k] = 255
#             else:
#                 outImage[i][k] = inImage[i][k] + value               # 확보된 영역에 진짜 이미지 삽입
#     display()
#
# def darkFile():
#     global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
#     outW = inW
#     outH = inH
#     outImage=[]
#     tmpList = []
#     for i in range(outH):
#         tmpList = []
#         for k in range(outW):
#             tmpList.append(0)
#         outImage.append(tmpList)        # 램에 0으로 영역 확보
#     #######################################
#     # 진짜 영상 처리 알고리즘 구현 ####
#     ######################################
#     value = askinteger('어둡게하기', '어둡게 할 값 ==>', minvalue=1, maxvalue=255)
#     for i in range(inH):
#         for k in range(inW):
#             if inImage[i][k] - value<0:
#                 outImage[i][k] = 0
#             else:
#                 outImage[i][k] = inImage[i][k] - value               # 확보된 영역에 진짜 이미지 삽입
#     display()
#
# def xFile():
#     global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
#     outW = inW
#     outH = inH
#     outImage=[]
#     tmpList = []
#     for i in range(outH):
#         tmpList = []
#         for k in range(outW):
#             tmpList.append(0)
#         outImage.append(tmpList)        # 램에 0으로 영역 확보
#     #######################################
#     # 진짜 영상 처리 알고리즘 구현 ####
#     ######################################
#     value = askinteger('밝게 할 비율',  '밝게 할 비율값 ==>', minvalue=1, maxvalue=255)
#     for i in range(inH):
#         for k in range(inW):
#             if inImage[i][k] * value>255:
#                 outImage[i][k] = 255
#             else:
#                 outImage[i][k] = inImage[i][k] * value
#     display()
#
# def yFile():
#     global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
#     outW = inW
#     outH = inH
#     outImage=[]
#     tmpList = []
#     for i in range(outH):
#         tmpList = []
#         for k in range(outW):
#             tmpList.append(0)
#         outImage.append(tmpList)        # 램에 0으로 영역 확보
#     #######################################
#     # 진짜 영상 처리 알고리즘 구현 ####
#     ######################################
#     value = askinteger('어둡게 할 비율',  '어둡게 할 비율값 ==>', minvalue=1, maxvalue=255)
#     for i in range(inH):
#         for k in range(inW):
#             outImage[i][k] = inImage[i][k] / value
#     display()
#
# def transformFile():
#     global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
#     outW = inW
#     outH = inH
#     outImage=[]
#     tmpList = []
#     for i in range(outH):
#         tmpList = []
#         for k in range(outW):
#             tmpList.append(0)
#         outImage.append(tmpList)
#     for i in range(inH):
#         for k in range(inW):
#             outImage[i][k] = 255-inImage[i][k]                # 확보된 영역에 진짜 이미지 삽입
#     display()
#
#
# def Gamma():
#     global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
#     outW = inW
#     outH = inH
#     outImage=[]
#     tmpList = []
#     for i in range(outH):
#         tmpList = []
#         for k in range(outW):
#             tmpList.append(0)
#         outImage.append(tmpList)        # 램에 0으로 영역 확보
#     #######################################
#     # 진짜 영상 처리 알고리즘 구현 ####
#     ######################################
#     value = askinteger('gamma*10',  'gamma(1~20) ==>', minvalue=1, maxvalue=20)
#     for i in range(inH):
#         for k in range(inW):
#             if int(inImage[i][k] **(value/10))>255:
#                 outImage[i][k] = 255
#             else:
#                 outImage[i][k] = int(inImage[i][k] **(value/10))
#     display()
#
# def cancelFile():
#     global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
#     pass
#
# def exitFile():
#     global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
#     pass
#
#
# def saveFile():
#     global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
#     pass
#


#전역 변수부
window, canvas, paper,filename = [None]*4
inImageR,inImageG, inImageB, outImageR,outImageG, outImageB =[[]]*6                        #부가변수
inW, inH, outW, outH = [0]*4                    #핵심변수

#메인 코드부
window = Tk()
window.geometry('400x400')
window.title('GIF영상처리 & 데이터분석 Ver 0.01')

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '열기',command = openFile)
# fileMenu.add_separator()
# fileMenu.add_command(label = '저장',command = saveFile)
# fileMenu.add_separator()
# fileMenu.add_command(label = '종료',command = exitFile)
# # fileMenu.add_separator()
# # fileMenu.add_command(label = '인쇄',command = printFile)
# # fileMenu.add_separator()
# # fileMenu.add_command(label = '명령 취소',command = cancelFile)
#
# pixelMenu = Menu(mainMenu)
# mainMenu.add_cascade(label = '화소점처리', menu = pixelMenu)
# pixelMenu.add_command(label = '동일영상',command =  euqal )
# pixelMenu.add_separator()
# pixelMenu.add_command(label = '밝게 하기',command = addImage)
# pixelMenu.add_separator()
# pixelMenu.add_command(label = '어둡게 하기',command = darkFile)
# pixelMenu.add_separator()
# pixelMenu.add_command(label = '곱셈',command = xFile)
# pixelMenu.add_separator()
# pixelMenu.add_command(label = '나눗셈',command = yFile)
# pixelMenu.add_separator()
# pixelMenu.add_command(label = '화소 반전',command = transformFile)
# pixelMenu.add_separator()
# pixelMenu.add_command(label = '감마',command = Gamma)
# # pixelMenu.add_separator()
# # pixelMenu.add_command(label = '파라볼라',command = parabolaCap)
# # pixelMenu.add_separator()
# # pixelMenu.add_command(label = '파라볼라',command = parabolaCup )
# #
# #
# # layoutMenu = Menu(mainMenu)
# # mainMenu.add_cascade(label = '레이아웃', menu = layoutMenu)
# # layoutMenu.add_command(label = '레이아웃 추가',command = newLayoutFile )
# # layoutMenu.add_separator()
# # layoutMenu.add_command(label = '레이아웃 삭제',command = deletLayoutFile)
# # layoutMenu.add_separator()
# # layoutMenu.add_command(label = '레이아웃 겹쳐보기',command = overlapLayoutFile)
# #
# # graphicMenu = Menu(mainMenu)
# # mainMenu.add_cascade(label = '그래픽', menu = graphicMenu)
# # graphicMenu.add_command(label = '문자입력',command = textFile)
# # graphicMenu.add_separator()
# # graphicMenu.add_command(label = '리샘플링',command = resampleFile)
# # graphicMenu.add_separator()
# # graphicMenu.add_command(label = '영역선택',command = areaFile)
# # graphicMenu.add_separator()
# # graphicMenu.add_command(label = '영역정보',command = areaInfoFile)
# # graphicMenu.add_separator()
# # graphicMenu.add_command(label = 'integration',command = integrationFile)
#
#
# # 영상처리를 위한 알고리즘이 어떤 것이 있는지 알아보고 메뉴에 추가해 놓기 15개
#

window.mainloop()
