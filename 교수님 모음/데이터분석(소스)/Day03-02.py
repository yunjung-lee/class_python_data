# 키보드 이벤트
# 텍스트 상자(Entry)에 숫자만 입력되도록 하기.
from tkinter import *
from tkinter import messagebox
# 함수 선언부
def keyEvent(e) :
    global textBox
    key = chr(e.keycode)
    if '0' <= key <= '9' :
        pass
    else :
        txt = textBox.get()
        txt = txt[:-1]
        textBox.delete(0, 'end') # 상자 다 지우기
        textBox.insert(0, txt)

# 변수 선언부
window = None # 메인 윈도창
# 메인 코드부
window = Tk();  window.geometry('400x400');
textBox = Entry(window)
textBox.bind("<KeyRelease>", keyEvent)

textBox.pack(anchor=CENTER)
window.mainloop()
