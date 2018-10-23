from tkinter import  *

#변수 선언
i=0
imageList = ['1.gif','2.gif','3.gif','4.gif','5.gif','6.gif']
photoData = imageList[i]



#함수선언
def clickL():
    global i
    global photoData
    i-=1
    if i > 0 :
        photoData = imageList[i]
    else:
        photoData = imageList[0]
    photo = PhotoImage(file=photoData)
    lable5.configure(image=photo)
    lable5.image=photo

def clickN():
    global i
    global photoData
    i+=1
    if i <5:
        photoData = imageList[i]
    else:
        photoData = imageList[5]
    photo = PhotoImage(file=photoData)
    lable5.configure(image=photo)
    lable5.image=photo

#메인코드
window = Tk()
window.geometry('400x400')

lable1 = Button(window, text = '<Last',command = clickL)
lable2 = Button(window, text = 'Next>',command = clickN)
photo = PhotoImage(file=photoData)
lable5 = Label(window, image=photo)


lable1.place(x=100,y=10)
lable2.place(x=250,y=10)
lable5.place(x=50,y=50)

window.mainloop()


