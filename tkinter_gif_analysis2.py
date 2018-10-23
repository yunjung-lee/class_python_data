## GIF 이미지 뷰어 & 데이터 분석 ##

from  tkinter import *

from  tkinter.filedialog import *

import operator




## 함수 선언부

def openFile():

    global photo

    filename = askopenfilename(parent=window,

                    filetypes=(("GIF파일", "*.gif"), ("모든파일", "*.*")))

    photo = PhotoImage(file=filename)

    pLabel.configure(image=photo)

    pLabel.image=photo




def exitFile():

    window.quit()

    window.destroy()




def analyzeGIF() :

    global photo

    rDic, gDic, bDic = {}, {}, {}  # 색상:개수 딕셔너리

    xSize = photo.width();  ySize = photo.height()

    for  i  in  range(xSize) :

        for  k  in  range(ySize) :

            r,g,b = photo.get(i,k)

            if  r  in  rDic :

                rDic[r] += 1

            else :

                rDic[r] = 1

            if  g  in  gDic :

                gDic[g] += 1

            else :

                gDic[g] = 1

            if  b  in  bDic :

                bDic[b] += 1

            else :

                bDic[b] = 1

    rList = sorted(rDic.items(), key=operator.itemgetter(1))

    gList = sorted(gDic.items(), key=operator.itemgetter(1))

    bList = sorted(bDic.items(), key=operator.itemgetter(1))

    print('최소/최다 출현 r픽셀값:', rList[0], rList[-1])

    print('최소/최다 출현 g픽셀값:', gList[0], gList[-1])

    print('최소/최다 출현 b픽셀값:', bList[0], bList[-1])




    rSum = 0

    for  item in rList :

        rSum += item[0]*item[1]

    rAvg = rSum / (xSize*ySize)




    gSum = 0

    for item in gList:

        gSum += item[0] * item[1]

    gAvg = gSum / (xSize * ySize)




    bSum = 0

    for item in bList:

        bSum += item[0] * item[1]

    bAvg = bSum / (xSize * ySize)

    print('r,g,b픽셀 평균값:', rAvg, gAvg, bAvg)




    rList = sorted(rDic.items(), key=operator.itemgetter(0))

    gList = sorted(gDic.items(), key=operator.itemgetter(0))

    bList = sorted(bDic.items(), key=operator.itemgetter(0))

    rStream, gStream, bStream  = [], [], []

    for item in rList :

        for i in range(item[1]) :

            rStream.append(item[0])

    for item in gList:

        for i in range(item[1]):

            gStream.append(item[0])

    for item in bList:

        for i in range(item[1]):

            bStream.append(item[0])

    midPos = int((xSize * ySize) / 2)

    print('r,g,b픽셀 중위수:', rStream[midPos], gStream[midPos], bStream[midPos])







## 전역 변수부

photo = None




## 메인 코드부

window = Tk() ; window.geometry('400x400')

# 빈 사진 준비

photo = PhotoImage()

pLabel = Label(window, image=photo)

pLabel.pack(expand=1, anchor=CENTER)




mainMenu = Menu(window);window.config(menu=mainMenu)

fileMenu = Menu(mainMenu);mainMenu.add_cascade(label='파일', menu=fileMenu)

fileMenu.add_command(label='열기(Ctrl+O)', command=openFile)

fileMenu.add_separator()

fileMenu.add_command(label='GIF 데이터 분석', command=analyzeGIF)

fileMenu.add_separator()

fileMenu.add_command(label='종료(Ctrl+X)', command=exitFile)







window.mainloop()