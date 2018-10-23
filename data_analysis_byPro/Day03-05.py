## GIF 이미지 뷰어 ##
from  tkinter import *
from  tkinter.filedialog import *
## 함수 선언부
def openFile():
    filename = askopenfilename(parent=window,
                    filetypes=(("GIF파일", "*.gif"), ("모든파일", "*.*")))
    photo = PhotoImage(file=filename)
    pLabel.configure(image=photo)
    pLabel.image=photo

def exitFile():
    window.quit()
    window.destroy()

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
fileMenu.add_command(label='종료(Ctrl+X)', command=exitFile)


window.mainloop()
