# 복습퀴즈1. 800x800 화면에서 거북이가 다음 정보를 소유하도록 한다.
# 	[거북이개체, (시작x,y), (끝x,y), (r,g,b), 크기]
#      20마리를 생성해서 리스트에 저장한 후에, 각각 이동하도록 한다.

import turtle; import random
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











