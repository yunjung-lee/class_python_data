# 마우스 이벤트 처리 1
from tkinter import *
from tkinter import messagebox
# 함수 선언부
def clickLeft(event) :
    xCor = event.x  ;  yCor = event.y;    mButton = event.num
    txt = ""  # 빈 문자열 준비
    if mButton == 1 :
        txt += '왼쪽 '
    elif mButton == 2 :
        txt += '가운데 '
    else:
        txt += '오른쪽 '
    txt +=  '를 ' + str(xCor) + ',' + str(yCor) + '에서 클릭함'
    messagebox.showinfo("마우스", txt)

# 변수 선언부
window = None # 메인 윈도창
# 메인 코드부
window = Tk();  window.geometry('400x400');

photo = PhotoImage(file = "D:\images\dog.gif")
label1 = Label(window, image=photo)
label1.pack(anchor=CENTER)
label1.bind("<Button>", clickLeft)




window.mainloop()
