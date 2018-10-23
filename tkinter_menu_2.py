# 메뉴 처리

from tkinter import *

from tkinter.simpledialog import *

from tkinter.filedialog import *


def openFile():
    filename = askopenfilename(parent=window,

                               filetypes=(("GIF파일", "*.gif"), ("모든파일", "*.*")))

    label1.configure(text=filename)


def exitFile():
    print('[종료] 선택함...')


def editFile(num):
    if num == 1:
        value = askinteger('제목', '설명-->', minvalue=1, maxvalue=255)

        label1.configure(text=str(value))


window = Tk();
window.geometry('400x400');

mainMenu = Menu(window)

window.config(menu=mainMenu)

label1 = Label(window, text='입력된 값:')

label1.pack()

fileMenu = Menu(mainMenu)

mainMenu.add_cascade(label='파일', menu=fileMenu)

fileMenu.add_command(label='열기(Ctrl+O)', command=openFile)

fileMenu.add_separator()

fileMenu.add_command(label='종료(Ctrl+X)', command=exitFile)

editMenu = Menu(mainMenu)

mainMenu.add_cascade(label='편집', menu=editMenu)

editMenu.add_command(label='숫자입력', command=lambda: editFile(1))

editMenu.add_command(label='잘라내기', command=lambda: editFile(2))

editMenu.add_command(label='붙여넣기', command=lambda: editFile(3))

window.mainloop()
