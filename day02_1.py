#튜플 :  위치같은 것 몇개만 사용
#튜플이 리스트로 바뀔 수 있으나 바꿔야한 경우는 리스트로 만드는게 좋다
#딕셔너리는 중요하고 유용하다.
#p199 딕셔너리:자료형에 유용하다.
#            {키:벨류} 쌍으로 이뤄져 있다.
#             키가 중복이 안된다.=>가장 중요한 특징
#            순서가 없다.=>효율적 저장을 위해 저장 순서를 정하지 않는다.
#셋 : 딕셔너리에서 키만 모아놓은 형태
#p221예제


import operator

##변수 선언##

ttList = [('토마스',5),('헨리',8),('에드워드',9),('토마스',4),('헨리',2)]        #리스트 안에 튜플

tDic, tList = {},[]
totalRank,currentRank = 0,0

##메인 코드##
for tmpTup in ttList :
    tName = tmpTup[0] #기차의 이름 : 키
    tWeight = tmpTup[1] #기차 작업량
    if tName in tDic:
        tDic[tName]+=tWeight
    else:
        tDic[tName ] = tWeight
tList = sorted(tDic.items(),key=operator.itemgetter(1),reverse=True)
#리스트 안의 딕셔너리쌍을 정렬하는데 정렬기준(key)를 1위치에 있는 것으로,reverse=>역순으로)
#많이 사용하는 코드

# print(tList[0],currentRank)

for i in range(0,len(tList)):
    totalRank += 1
    if tList[i][1] ==tList[i-1][1] :
        pass
    else:
        currentRank = totalRank
    print(tList[i],currentRank)













