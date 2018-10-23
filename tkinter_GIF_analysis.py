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

    countList = sorted(rDic.items(), key=operator.itemgetter(1))

    print('최소출현 r픽셀값:', countList[0])

    print('최다출현 r픽셀값:', countList[-1])




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