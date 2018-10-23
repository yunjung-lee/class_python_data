import turtle
import random

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

# num = int(input('숫자-->'))
# binary = bin(num)
#
# curX = swidth/2
# curY = 0
#
# for i in range(len(binary)-2):
#     turtle.goto(curX,curY)
#     if num & 1 :                        #&연산자
#         turtle.color('red')
#         turtle.turtlesize(2)
#     else:
#         turtle.color('blue')
#         turtle.turtlesize(1)
#     turtle.stamp()
#     curX-=50
#     num >>=1                            #>> 연산자
#
# turtle.done()
#
# #입력된 숫자를 8진수 거북이로 표현

num1 = int(input('숫자1-->'))
b1 = bin(num1)
num2 = int(input('숫자2-->'))
b2 = bin(num2)
num3=num1&num2
b3=bin(num3)
print(b3)
# a=[b1[num1],b2[num2],b3[num3]]
a=[b1,b2,b3]

curX = swidth/2-50
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


