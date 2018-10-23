##정방형 raw이미지 처리
##그레이 스케일: 밝기만 표현(0:블랙,255: 화이트)
##밝게 : 숫자를 더함,어둡게 : 숫자를 뺌

from  tkinter import *
import os.path
import math
from tkinter.filedialog import *

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
    canvas.create_image((outW/2,outH/2),image = paper, state = 'normal')
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





def saveFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass

def exitFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass

def printFile():
    global window, canvas, paper,filename,inImage, outImage,inW, inH, outW, outH
    pass

def cancelFile():
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
fileMenu.add_separator()
fileMenu.add_command(label = '인쇄',command = printFile)
fileMenu.add_separator()
fileMenu.add_command(label = '명령 취소',command = cancelFile)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '영상처리', menu = editMenu)
editMenu.add_command(label = '밝게하기',command = brightFile )
editMenu.add_separator()
editMenu.add_command(label = '어둡게하기',command = darkFile)
editMenu.add_separator()
editMenu.add_command(label = '반전하기',command = reversFile)
# editMenu.add_separator()
# editMenu.add_command(label = '확대',command = zoominFile)
# editMenu.add_separator()
# editMenu.add_command(label = '축소',command = zoomoutFile)
# editMenu.add_separator()
# editMenu.add_command(label = '각도',command = angleFile)
# editMenu.add_separator()
# editMenu.add_command(label = '비율',command = ratioFile)
# editMenu.add_separator()
# editMenu.add_command(label = '제목',command = titleFile)
# editMenu.add_separator()
# editMenu.add_command(label = '사진정보',command = infoFile )
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
# graphicMenu = Menu(mainMenu)
# mainMenu.add_cascade(label = '그래픽', menu = graphicMenu)
# graphicMenu.add_command(label = '문자입력',command = textFile)
# graphicMenu.add_separator()
# graphicMenu.add_command(label = '리샘플링',command = resampleFile)
# graphicMenu.add_separator()
# graphicMenu.add_command(label = '영역선택',command = areaFile)
# graphicMenu.add_separator()
# graphicMenu.add_command(label = '영역정보',command = areaInfoFile)
# graphicMenu.add_separator()
# graphicMenu.add_command(label = 'integration',command = integrationFile)


# 영상처리를 위한 알고리즘이 어떤 것이 있는지 알아보고 메뉴에 추가해 놓기 15개


window.mainloop()
