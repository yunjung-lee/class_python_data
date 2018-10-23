# 퀴즈1. 1부터 100까지 3의 배수의 합계.
# 클래스 선언부

# 함수 선언부
# (전역) 변수 선언부 (초기화)
start, end, hap = [0] * 3

# 메인 코드부
if __name__ == '__main__' :
    for  i  in  range(1, 101, 1) :
        if  i%3 != 0 :
            pass
        else :
            hap += i

    print(hap)
