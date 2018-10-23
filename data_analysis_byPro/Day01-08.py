import turtle; import random
# 전역 변수
myTutle, tX, tY, tColor, tSize, tShape = [None] * 6
shapeList = []  # 거북이 모양 리스트...
playerTurtles = []  # 거북이 100마리.. 2차원 리스트
swidth, sheight = 500,500
# 메인 코드
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth, sheight);
shapeList = turtle.getshapes()
for i in range(100) :
    random.shuffle(shapeList)
    myTutle = turtle.Turtle(shapeList[0])
    tX = random.randrange(-swidth/2, swidth/2)
    tY = random.randrange(-sheight / 2, sheight / 2)
    r=random.random();g=random.random();b=random.random();
    tSize = random.randint(1,3)
    playerTurtles.append( [myTutle, tX, tY, tSize, r, g, b] )

for tList in playerTurtles :
    myTutle = tList[0]
    myTutle.color( (tList[4],tList[5], tList[6]))
    myTutle.pencolor((tList[4], tList[5], tList[6]))
    myTutle.turtlesize(tList[3])
    myTutle.goto(tList[1], tList[2])

turtle.done()











