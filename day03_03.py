#메뉴처리
from tkinter import *
def openFile():
    print('[열기] 선택함.')
def exitFile():
    print('[종료] 선택함.')
# def copyFile():
#     print('[복사] 선택함.')
# def cutFile():
#     print('[잘라내기] 선택함.')
# def pasteFile():
#     print('[붙여넣기] 선택함.')
def editFile(num) :
    print(str(num)+'선택함.')

window = Tk()

mainMenu = Menu(window)
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '파일', menu = fileMenu)
fileMenu.add_command(label = '열기(Ctrl+o)',command = openFile)               #command : 함수 호출구문,()를 사용 못한다.
fileMenu.add_separator()
fileMenu.add_command(label = '종료(Ctrl+x)',command = exitFile)

#[편집]메뉴 추가
editMenu = Menu(mainMenu)
mainMenu.add_cascade(label = '편집', menu = editMenu)
editMenu.add_command(label = '복사',command = lambda : editFile(1) )               #command : lambda를 활용해서 ()를 사용
editMenu.add_separator()
editMenu.add_command(label = '잘라내기',command = lambda : editFile(2))
editMenu.add_separator()
editMenu.add_command(label = '붙여넣기',command = lambda : editFile(3))




window.mainloop()