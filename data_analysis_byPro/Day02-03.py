from tkinter import *

def clickButton() :
    print('나 불렀어요?')

window = Tk()
window.geometry('400x400')


label1 = Button(window, text="ㅋㅋㅋㅋㅋ", command=clickButton)
photo = PhotoImage(file='d:/images/dog.gif')
label2 = Label(window, image=photo)


label1.pack();label2.pack()
window.mainloop()