##통계 기반 데이터 분석(부제 : 영상처리를 통한 데이터 분석 및 통계 처리)##

#복습 퀴즈1. 800x800화면에서 거북이가 다음 정보를 소유하도록 한다.
# [거북이개체, (시작x,y), 끝(x,y), (r,g,b) ,크기]
#20 마리를 생성해서 리스트에 저장한 후에 ,각각 이동하도록 한다.

import turtle
import random

# myTurtle = 0
# #tStart, tEnd = (0,0),(0,0)
# sX,sY = 0,0
# eX,eY = 0,0
# r,g,b,tSize = [0]*4
# tWidth,tHeight = 800,800
#
#
# myList=[]
# shape = []
#
#
# turtle.shape('turtle')
# turtle.setup(width=tWidth + 30, height=tHeight + 30)
# turtle.screensize(tWidth, tHeight)
# turtle.penup()
# turtle.left(90)
# sList = turtle.getshapes()
#
#
# for i in range(20):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     tStart = (0,0)
#     sX = random.randrange(-tWidth/2,tWidth/2)
#     sY = random.randrange(-tHeight/2,tHeight/2)
#     eX = random.randrange(-tWidth/2,tWidth/2)
#     eY = random.randrange(-tHeight/2,tHeight/2)
#     random.choice(sList)
#     myTurtle=turtle.Turtle(sList[0])
#     tSize = random.randint(1,5)
#     myList.append([myTurtle,tX,tY,tSize,r,g,b,tStart])
#
# for tList in myList:
#     myTurtle=tList[0]
#     myTurtle.color((tList[4],tList[5],tList[6]))
#     myTurtle.pencolor((tList[4],tList[5],tList[6]))
#     myTurtle.turtlesize(tList[3])
#     myTurtle.goto(tList[8])
###############잘 안돌아감##########################################

##############교수님 버전################################################
# 전역 변수

myTutle, sX, sY, eX, eY, tColor, tSize, tShape = [None] * 8

shapeList = []  # 거북이 모양 리스트...

playerTurtles = []  # 거북이 20마리.. 2차원 리스트

swidth, sheight = 300,300

# 메인 코드

turtle.setup(width=swidth+30, height=sheight+30)

turtle.screensize(swidth, sheight);

shapeList = turtle.getshapes()

for i in range(10) :

    random.shuffle(shapeList)

    myTutle = turtle.Turtle(shapeList[0])

    sX = random.randrange(-swidth/2, swidth/2)

    sY = random.randrange(-sheight / 2, sheight / 2)

    eX = random.randrange(-swidth/2, swidth/2)

    eY = random.randrange(-sheight / 2, sheight / 2)

    r=random.random();g=random.random();b=random.random();

    tSize = random.randint(1,3)

    playerTurtles.append( [myTutle, (sX, sY), (eX, eY), (r, g, b), tSize] )




for tList in playerTurtles :

    myTutle = tList[0]

    myTutle.color( (tList[3][0],tList[3][1], tList[3][2]))

    myTutle.pencolor((tList[3][0],tList[3][1], tList[3][2]))

    myTutle.turtlesize(tList[4])

    myTutle.penup()

    myTutle.goto(tList[1][0], tList[1][1])

    myTutle.stamp()

    myTutle.pendown()

    myTutle.goto(tList[2][0], tList[2][1])




turtle.done()






#복습 퀴즈2. 구구단을 처리하되, 각 결과의 앞자리 ~뒷자리 까지 합계로 출력한다.
#예 :  2x1=2(값 2까지의 숫자의 합계 : 0+1+2=3)
##########################문제 이해를 잘못함##################################
for i in range (2,10):
    print('##',i,'단 ##')
    for k in range (1,10):
        print(i,'x',k,'=',sum(list(filter(lambda x : x ,range(i*k+1)))))

# 복습퀴즈2. 구구단을 처리하되, 각 결과의 앞자리~뒷자리까지 합계로 출력한다.

#    예)  2x1=3   (값2를 02로 취급해서 0부터 2까지의 합계 : 0+1+2 = 3)

#          2x2=10 (값2를 02로 취급해서 0부터 2까지의 합계 : 0+1+2+3+4 = 10)

#          ...

#          2x9=36  (값18을 1부터 8까지 : 1+2+3+4+5+6+7+8=36)

#          ...

#          8x8=15  (값64를 6부터 4까지 : 6+5+4 = 15)




for i  in  range(2, 10) :

    print('##', i, '단##')

    for k  in range(1, 10) :

        res = i*k

        if res < 10 :

            start = 0

        else :

            start = int(res / 10)

        end = res % 10

        if start > end :

            start, end = end, start




        hap = 0

        for num in range(start, end+1) :

            hap += num




        print(i, 'x', k, '=', hap)

    print('\n')







#복습 퀴즈 3. 행과 열의 크기를 입력받고, 크기만큼 가로 및 세로로 지그재그로 1부터 출력한다.
#예 : 3,4 를 입력하면
#    1 2 3 4
#    8 7 6 5
#    9 10 11 12

#    1 6 7 12
#    2 5 8 11
#    3 4 9 10

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


