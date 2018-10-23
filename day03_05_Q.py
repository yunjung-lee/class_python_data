#p323동물 투표하기

from tkinter import *
from tkinter.filedialog import *

#변수선언
pList=['dog.gif',
       'cat.gif',
       'rabbit.gif']
s='d:/data_analysis/gif/GIF/'


#함수선언
def radio():
    if var.get()==1:
        filename = s + pList[0]
        photo = PhotoImage(file=filename)
        lable2.configure(image=photo)
        lable2.image = photo
    elif var.get()==2:
        filename = s + pList[1]
        photo = PhotoImage(file=filename)
        lable2.configure(image=photo)
        lable2.image = photo
    else:
        filename = s + pList[2]
        photo = PhotoImage(file=filename)
        lable2.configure(image=photo)
        lable2.image = photo





#메인코드
window = Tk()
window.geometry('400x600')

text = Label(window, text = "좋아하는 동물 투표하기",fg = 'blue',font =('궁서체',20))
var = IntVar()
rb1 = Radiobutton(window,text = '강아지',variable = var, value = 1, command = radio)
rb2 = Radiobutton(window,text = '고양이',variable = var, value = 2, command = radio)
rb3 = Radiobutton(window,text = '토끼',variable = var, value = 3, command = radio)

photo = PhotoImage(file='d:/dog.gif')
lable2 = Label(window, image=photo)

text.pack()
rb1.pack(pady=5, anchor = CENTER)
rb2.pack(pady=5, anchor = CENTER)
rb3.pack(pady=5,anchor = CENTER)
lable2.pack(pady=5, anchor = CENTER)

window.mainloop()


###
