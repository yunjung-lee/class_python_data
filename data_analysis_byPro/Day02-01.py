import operator
## 변수 선언 ##
ttList = [ ('토마스', 5), ('헨리', 8), ('에드워드',9), ('토마스', 4),
           ('헨리', 2)]
tDic, tList = {}, []
totalRank, currentRank = 1, 1
## 메인 코드 ##
for tmpTup in ttList :
    tName = tmpTup[0] # 기차 이름 : 키
    tWeight = tmpTup[1] # 기차 작업량
    if tName in tDic :
        tDic[tName] += tWeight
    else :
        tDic[tName] = tWeight
tList = sorted(tDic.items(), key = operator.itemgetter(1), reverse =True )

print(tList[0], currentRank)
for i in range(1, len(tList)) :
    totalRank += 1
    if tList[i][1] == tList[i-1][1] :
        pass
    else :
        currentRank = totalRank
    print(tList[i], currentRank)

