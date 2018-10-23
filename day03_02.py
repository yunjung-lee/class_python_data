#마우스 이벤트 처리

from tkinter import  *
from tkinter import messagebox

#함수선언
def keyEvent(e):
    global textBox
    key = chr(e.keycode)
    if '0'<=key <='9':
        pass
    else:
        txt = textBox.get()
        txt = txt[:-1]
        textBox.delete(0,'end')              #상자 다 지우기
        textBox.insert(0,txt)
#변수선언

    #메인 윈도우창
window = None


#메인코드
window = Tk()
window.geometry('400x400')


textBox = Entry(window)
textBox.bind('<KeyRelease>',keyEvent)                   #키보드를 누를 때와 땔 때 구분해서 사용된다.(예민하게 사용시)

textBox.pack(anchor = CENTER)

window.mainloop()



