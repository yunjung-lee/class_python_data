#리스트 연습

import random
# mylist=[]
#
# mylist.append(10)
# mylist.append('20')
# mylist.append([1,2,3])
#
# print(mylist)

lotto = [] #45 -->6
# for i in range(6):
# #    num=random.randrange(1,46) : #아래와 동일 결과
#     num = random.randint(1, 45)
#     lotto.append(num)
# #중복을 허용

while True:
    num = random.randint(1, 45)
    if lotto.count(num) >0 :
        continue                    #다시 실행
    lotto.append(num)
    if len(lotto) >=6 :
        break
lotto.sort()                        #sort()는 배열을 바꿀 뿐 출력에 사용하면 None을 반환한다.
print(lotto)





