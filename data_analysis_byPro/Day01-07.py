# 2차원 리스트 조작 (완전 중요!, 짱!, 캡! 중요)
# 3x4 크기의 빈 리스트를 만들자.
ROW = int(input('행-->'))
COL = int(input('열-->'))

myList = []  # 2차원 리스트
tmpList = []

for i in range(ROW) :
    tmpList = []
    for k in range(COL) :
        tmpList.append(0)
    myList.append(tmpList)


for i in range(ROW) :
    for k in range(COL) :
        print("%2d " % myList[i][k] , end='')
    print()



