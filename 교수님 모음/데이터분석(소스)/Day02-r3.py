# 복습퀴즈3(심화). 행과 열의 크기를 입력받고, 크기만큼 가로 및 세로로 지그재그로
#    1부터 출력한다.
#     예) 3, 4를 입력하면
#          1   2  3   4
#          8   7  6   5
#          9 10 11 12
#
#          1   6  7  12
#          2   5  8  11
#          3   4  9  10

ROW = int(input('행-->'))
COL = int(input('열-->'))

myList = []  # 2차원 리스트
tmpList = []


## 1번 출력
## 빈 리스트 생성
for i in range(ROW) :
    tmpList = []
    for k in range(COL) :
        tmpList.append(0)
    myList.append(tmpList)

value = 1
for i in range(ROW) :
    if i % 2 == 0:
        for k in range(COL) :
            myList[i][k] = value
            value += 1
    else :
        for k in range(COL-1, -1, -1) :
            myList[i][k] = value
            value += 1

for i in range(ROW) :
    for k in range(COL) :
        print("%2d " % myList[i][k] , end='')
    print()

print()
## 2번 출력
## 빈 리스트 생성
myList = []  # 2차원 리스트
tmpList = []
for i in range(ROW) :
    tmpList = []
    for k in range(COL) :
        tmpList.append(0)
    myList.append(tmpList)

value = 1
for i in range(COL) :
    if i % 2 == 0:
        for k in range(ROW) :
            myList[k][i] = value
            value += 1
    else :
        for k in range(ROW-1, -1, -1) :
            myList[k][i] = value
            value += 1

for i in range(ROW) :
    for k in range(COL) :
        print("%2d " % myList[i][k] , end='')
    print()