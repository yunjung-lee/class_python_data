##gif이미지 뷰어##

from tkinter import  *
from tkinter.filedialog import *
#함수 선언부

def openFile():
    filename = askopenfilename(parent = window, filetypes = (('GIF파일','*.gif'),('모든파일','*.*')))
 #위의 경로의 파일을 보이기 함
    photo = PhotoImage(file = filename)             #3줄은 구문처럼 외우기
    pLabel1.configure(image = photo)
    pLabel1.image = photo


def exitFile():
    window.quit()
    window.destroy()                                #안에 있는 자료까지 없애는 구문(모두 없애야 한다.항상 두개를 같이)
##메인 코드부
window = Tk()
window.geometry('400x400')

photo = PhotoImage()
pLabel1 = Label(window, image = photo)
pLabel1.pack(expand = 1, anchor = CENTER)                   # 빈 사진 위치 준비

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '열기(Ctrl+o)',command = openFile)
fileMenu.add_separator()
fileMenu.add_command(label = '종료(Ctrl+x)',command = exitFile)



window.mainloop()