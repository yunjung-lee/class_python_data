#p194 : 리스트 활용
#거북이의 정보(모양,크기,색,...)가 리스트임
import turtle
import random
#전역변수
myTurtle, tX, tY, tColor, tSize, tShape = [None]*6

shape = []              #거북이 모양 리스트.,,,
playerTurtle = []       #거북이 100마리 ....2차원 리스트
swidth, sheight = 500,500

#메인코드
turtle.shape('turtle')
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.left(90)
shapeList = turtle.getshapes()

# print(shapeList)

for i in range ( 100):
    random.shuffle(shapeList)                   #shuffle대신 choice를 사용할 수 있다.
    myTurtle = turtle.Turtle(shapeList[0])
    tX = random.randrange(-swidth/2,swidth/2)
    tY = random.randrange(-sheight/2,sheight/2)
    r =random.random()
    g = random.random()
    b = random.random()
    tSize=random.randint(1,3)
    playerTurtle.append([myTurtle,tX,tY,tSize,r,g,b])

for tList in playerTurtle:
    myTurtle=tList[0]
    myTurtle.color((tList[4],tList[5],tList[6]))
    myTurtle.pencolor((tList[4],tList[5],tList[6]))
    myTurtle.turtlesize(tList[3])
    myTurtle.goto(tList[1],tList[2])

turtle.done()