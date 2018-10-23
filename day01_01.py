#1부터 100까지 3의 배수의 합계

# 클래스 선언부(객체지양 : 향후 코드 분석)


#함수 선언부


# (전역)변수 선언부 (초기화)
start,end,hap = [0] *3


#a,b=[],[]

#메인 코드부
if __name__=='__main__' :
    for i in range(1,101) :
        if i % 3 ==0:
            hap += i
        else:
            pass
    # 같은 내용
    # for i in range(1,101) :
    #     if i % 3 !==0:
    #         pass
    #     else:
    #         hap += i

print(hap)

