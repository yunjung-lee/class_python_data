#거북이 복습하기

#관례상 import는 코드 헤더에 몰아서 하는 것이 좋다.
import turtle
import random

#함수 선언
def clickLeft(x,y): #파라미터, 클릭한 위치
    turtle.goto(x,y)
    r = random.random() #0~0.99999
    g = random.random()
    b = random.random()
    turtle.pensize(random.randint(0,10))
    turtle.pencolor((r,g,b))    #:파라메터를 튜플로 넘기기 위해 이중()

def clickRight(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def clickMiddle(x,y):
    r = random.random()  # 0~0.99999
    g = random.random()
    b = random.random()
    turtle.color((r,g,b))

# def clickdouble(x,y):
#     turtle.stemp()



#변수 선언(소문자로 시작 : 변수 선언은 '_'로 분리 or 대소문자로 구분(java))
#행구분은  ;
#pSize = 0
#pen_size = 0
penSize = 0
#r,b,g = 0,0,0
r,b,g = [0]*3

#메인 선언(시작의 '__'=>시스템의 변수,'_'=>고유변수선언)
if __name__ =='__main__' :
    turtle.title('거북이가 그리기')
    turtle.shape('turtle')

#이벤트(작은 사건들 : 클릭) 생성
    turtle.onscreenclick(clickLeft, 1 )
    turtle.onscreenclick(clickRight, 3)
    turtle.onscreenclick(clickMiddle, 2)
    # turtle.onscreenclick(clickdouble,btn=3)
    #clickLeft : 콜백 또는 리슨너라고 부름



turtle.done()