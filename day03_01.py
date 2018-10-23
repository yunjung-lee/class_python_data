#마우스 이벤트 처리 1

from tkinter import  *
from tkinter import messagebox

#함수선언
def clickLeft(event):
    xCor = event.x
    yCor = event.y
    mButton = event.num
    txt = ''                                                    #빈 문자열 준비
    if mButton==1:
        txt+='왼쪽'
    elif mButton==2:
        txt +='가운데'
    else:
        txt += '오른쪽'

    txt += '를 ' + str(xCor) + ',' +str(yCor) + '에서 클릭함'

    messagebox.showinfo('마우스', txt)

def keyEvent(event):
    code = event.keycode
    messagebox.showinfo('키보드', chr(code))

#변수선언

    #메인 윈도우창
window = None


#메인코드
window = Tk()
window.geometry('400x400')

photo = PhotoImage(file="1.gif")
label1 = Label(window, image = photo)
    #bind('입력 방법',실행 함수)
label1.bind('<Button>',clickLeft)

window.bind("<Key>", keyEvent)



label1.pack(expand = 1, anchor=CENTER)
    # window 에 써지는 모든 이벤트를 감지
window.mainloop()





























