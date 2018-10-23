###GUI#######
###tkinter :  os를 가리지 않고 동일한 윈도우를 띄운다.#####

from tkinter import *

def clickButton():
    print('나 불렀어요?')

window = Tk()
window.geometry('400x400')                  #window 환경의 크기 설정 :  문자로 입력한다.


lable1=Button(window, text = 'zzzz', command = clickButton)
photo = PhotoImage(file='d:/dog.gif')
lable2 = Label(window, image=photo)



lable1.pack()
lable2.pack()
window.mainloop()