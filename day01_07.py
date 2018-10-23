#2차원 리스트 조작(완전 중요!.중요!!!!)
#3x4크기의 빈 리스트를 만들자.

# myList = [
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0]
#     ]

ROW=int(input('행-->'))                                   #대문자 사용 = 상수 의미(고치지 않는다.)
COL=int(input('열-->'))
myList =[]
temList =[]
for i in range (ROW):
    temList=[]                          #배열의 초기화
    for k in range(COL):
        temList.append(0)
    myList.append(temList)
print(myList)






