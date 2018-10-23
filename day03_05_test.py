####통계 기반 데이터 분석(부제 : 영상 처리를 통한 데이터 분석 및 통계 처리)####
# 1.복습 퀴즈  1. 숫자 정렬하기 p221
# 1~100까지 1000개의 숫자를 임의로 생성한 후에, 각 숫자의 발생 빈도를 순위로 매겨서 출력한다. 단, 동일 순위의 경우 1등,2등,2등,4등 식으로 부여한다
#
# 2.복습 퀴즈 문자열의 발생 빈도수 체크
# p241을 처리하되 딕셔너리를 사용하지 말고 리스트로만 처리한다.
#
# 3.복습 퀴즈 3(심화). 1부터 999까지 100개의 숫자를 임의로 생성한 후에, 뒤에서 두번째 숫자로 내림 차순 정렬한다.
#  단, 뒤에서 두번째 숫자가 동일하면 마지막 숫자로 정렬한다.
# (한자리 숫자의 경우 001식으로, 두자리 경우 011식으로 처리한다.)
#
# 예 092 838 071 004 037 --> 092 071 838 037 004

# 1.복습 퀴즈

import random
from collections import Counter
from operator import itemgetter

#변수선언
num,num1 = 0, 0
nList, sTuple = [],{}
totalRank,currentRank = 0,0

#함수선언

#메인코드
for i in range(1000):
    num = random.randint(1,101)
    nList.append(num)

sTuple = Counter(nList)
sTuple = sorted(sTuple.items(), key=itemgetter(1), reverse=True)
for i in range(0,len(sTuple)):
    totalRank += 1
    if sTuple[i][1] ==sTuple[i-1][1] :
        pass
    else:
        currentRank = totalRank
    # print(sTuple[i],currentRank)

# 2.복습 퀴즈 문자열의 발생 빈도수 체크
#변수선언

s = '''죽는 날까지 하늘을 우러러
한점 부끄럼이 없기를
잎새에 이는 바람에도
나는 괴로워했다
별을 노래하는 마음으로
모든 죽어가는 것을 사랑해야지
그리고 나한테 주어진 길을
걸어가야겠다.

오늘 밤에도 별이 바람에 스치운다'''

countDic,countList = [],[]
currentRank,totalRank = 0,0
sList = []



#함수선언

#메인코드
sList = list(s)

for i in sList:

    if '가'<= i <='힣':
        countList.append([i, sList.count(i)])

    else:
        pass
countList = list(set(countList))
countList.sort(key=lambda x : x[0])
countList.sort(key=lambda x : x[1],reverse=True)

print(countList)

for i in range(1,len(countList)):
    totalRank += 1
    if countList[i][1] ==countList[i-1][1] :
        pass
    else:
        currentRank = totalRank



# print(countList,currentRank)
#변수선언

#함수선언

#메인코드


