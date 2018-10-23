# 퀴즈1. 거북이 완성하기.
#
#    -  펜 색상, 두께 랜덤하게
#
#    -  거북이 색상과 크기는 가운데 버튼 누르면 바뀌기..
#
#   심화퀴즈1. 더블클릭하면 왔다 돌아가기.

import turtle
import random


def clickLeft(x,y):
    turtle.goto(x,y)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pensize(random.randint(0,10))
    turtle.pencolor((r,g,b))

def clickRight(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def clickMiddle(x,y):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r,g,b))

penSize = 0
r,b,g = [0]*3


if __name__ =='__main__' :
    turtle.title('거북이가 그리기')
    turtle.shape('turtle')

    turtle.onscreenclick(clickLeft, 1 )
    turtle.onscreenclick(clickRight, 3)
    turtle.onscreenclick(clickMiddle, 2)


turtle.done()

# 퀴즈2.p113.10번
#
# 심화퀴즈2.입력된 숫자를 8 진수 거북이로 표현.
#
# (거북이 크기 1~8)

#변수선언(전역변수)
num=0
swidth, sheight = 1000,300
curX,curY = 0,0

#메인코드
turtle.shape('turtle')
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.left(90)

num1 = int(input('숫자1-->'))
b1 = bin(num1)
num2 = int(input('숫자2-->'))
b2 = bin(num2)
num3=num1&num2
b3=bin(num3)
print(b3)
# a=[b1[num1],b2[num2],b3[num3]]
a=[b1,b2,b3]

curX = swidth/2
curY = 0

for j in  a :
    num=int(j,2)
    for i in range(len(j)-2):
        turtle.goto(curX,curY)
        if num & 1 :                        #&연산자
           turtle.color('red')
           turtle.turtlesize(2)
        else:
           turtle.color('blue')
           turtle.turtlesize(1)
        turtle.stamp()
        curX-=50
        num >>=1                            #>> 연산자
    curY -= 50
    curX = swidth/2

num = int(input('숫자-->'))
oct = oct(num)

for i in range(len(oct)-2):
    turtle.goto(curX,curY)
    if num & 1 :
        turtle.color('red')
        turtle.turtlesize(2)
    elif num & 2 :
        turtle.color('yellow')
        turtle.turtlesize(1)
    elif num & 3 :
        turtle.color('green')
        turtle.turtlesize(2)
    elif num & 5 :
        turtle.color('black')
        turtle.turtlesize(1)
    elif num & 6 :
        turtle.color('whit')
        turtle.turtlesize(1)
    elif num & 7 :
        turtle.color('purple')
        turtle.turtlesize(1)
    else:
        turtle.color('blue')
        turtle.turtlesize(1)
    turtle.stamp()
    curX-=50
    num >>=1

turtle.done()


# 퀴즈3.행, 열을 입력받고, 1 부터 채워나가기.출력 보기좋게.
#
# 2, 3 -->  1 2 3
#           4 5 6
#
# 심화퀴즈3.거꾸로 채우기...


ROW=int(input('행 -->'))
COL=int(input('열-->'))
a=0

myList =[]
temList = []

for i in range (ROW):
    temList=[]
    for k in range (COL):
        a += 1
        temList.append(a)
        print(a,end=' ')
    print("")
    myList.append(temList)

print(myList)

