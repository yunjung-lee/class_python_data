# 엑셀의 시트처럼 보이는 것 만들기.
from tkinter import *

csvList = [ [ '제목1', '제목2' , '제목3'],
            [ 111, 222, 333],
            [ 444, 555, 666],
            [ 777, 888, 999]     ]  # csv에서 읽어온 값

window = Tk()
rowNum = len(csvList)
colNum = len(csvList[0])
cellList = []
# 빈 시트 만들기
for i in range(0, rowNum) :
    tmpList = []
    for k in range(0, colNum) :
        ent = Entry(window,text='')
        tmpList.append(ent)
        ent.grid(row=i, column=k)
    cellList.append(tmpList)
# 시트에 리스트값 채우기. (= 각 엔트리에 값 넣기)
for i in range(0, rowNum) :
    for k in range(0, colNum) :
        cellList[i][k].insert(0, csvList[i][k])

window.mainloop()
