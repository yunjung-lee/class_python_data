## GIF 이미지 뷰어 ##
from tkinter import *
from tkinter.filedialog import *
import operator


## 함수 선언부
def openFile():
    global photo
    filename = askopenfilename(parent=window,
                               filetypes=(("GIF파일", "*.gif"), ("모든파일", "*.*")))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image = photo


def exitFile():
    window.quit()
    window.destroy()


def analyzeGIF():
    global photo
    rDic, gDic, bDic = {},{}, {}
    x = photo.width(); y = photo.height()
    for i in range(x):
        for k in range(y) :
            r, g, b = photo.get(i, k)
            if r in rDic :
                rDic[r] += 1
            else :
                rDic[r] = 1
    countList = sorted(rDic.items(), key=operator.itemgetter(1), reverse=True)
    print('*** GIF 영상 데이터 분석 ***')
    print('영상 크기 -->', x, y)
    print('최다개수 r픽셀값(VALUE, COUNT): ', countList[0])
    print('최소개수 r픽셀값(VALUE, COUNT): ', countList[-1])


# 변수 선언 부
photo = None

## 메인 코드부
window = Tk();
window.geometry('400x400')

# 빈 사진 준비
photo = PhotoImage()
pLabel = Label(window, image=photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window);
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu);
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기(Ctrl+O)', command=openFile)
fileMenu.add_command(label='데이터 분석', command=analyzeGIF)
fileMenu.add_separator()
fileMenu.add_command(label='종료(Ctrl+X)', command=exitFile)

window.mainloop()
