import turtle

# 변수 선언

num =0; swidth, sheight = 1000, 300; curX, curY = 0, 0

# 메인 코드

turtle.shape('turtle')

turtle.setup(width=swidth+30, height=sheight+30)

turtle.screensize(swidth, sheight);turtle.penup(); turtle.left(90)

num = int(input("숫자 -->"));binary = bin(num)

curX = swidth/2; curY = 0;




for i in range(len(binary)-2) :

    turtle.goto(curX,curY)

    if  num  &  1 :

        turtle.color('red'); turtle.turtlesize(2)

    else :

        turtle.color('blue'); turtle.turtlesize(1)

    turtle.stamp(); curX -= 50;

    num >>= 1







turtle.done()