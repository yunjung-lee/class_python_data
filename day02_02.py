#p241 예제02
#데이터 분석의 중요한 문자열 처리에서 이용
#시 또는 소설등의 빅데이터에서 빈도 분석하고 순위 매기기.

import operator


inStr = '''
님은 갔습니다. 아아, 사랑하는 나의 님은 갔습니다.
푸른 산빛을 깨치고 단풍나무 숲을 향하여 난 작은 길을 걸어서 차마 떨치고 갔습니다.
황금의 꽃같이 굳고 빛나던 옛 맹세는 차디찬 티끌이 되어서 한숨의 미풍에 날아갔습니다.
날카로운 첫 키스의 추억은 나의 운명의 지침을 돌려놓고 뒷걸음쳐서 사라졌습니다.
나는 향기로운 님의 말소리에 귀먹고 꽃다운 님의 얼굴에 눈멀었습니다.
사랑도 사람의 일이라 만날 때에 미리 떠날 것을 염려하고 경계하지 아니한 것은 아니지만, 이별은 뜻밖의 일이 되고 놀란 가슴은 새로운 슬픔에 터집니다.
그러나 이별을 쓸데없는 눈물의 원천으로 만들고 마는 것은 스스로 사랑을 깨치는 것인 줄 아는 까닭에 걷잡을 수 없는 슬픔의 힘을 옮겨서 새 희망의 정수박이에 들어부었습니다.
우리는 만날 때에 떠날 것을 염려하는 것과 같이 떠날 때에 다시 만날 것을 믿습니다.
아아, 님은 갔지마는 나는 님을 보내지 아니하였습니다.
제 곡조를 못 이기는 사랑의 노래는 님의 침묵을 휩싸고 돕니다.
'''

#퀴즈 1. 한글 글자의 빈도수를 출력하고 많은 빈도수의 차례대로 순위를 매기기(동일 순위 처리하기)
currentRank,totalRank = 0,0
countList={}
countList2={}
strList = []
strList2 = []
strList = list(inStr)
sList = []
strList2 = inStr.split()
print(strList2)


for i in strList:
    if '가'<=i <='힣':
        if i in countList:
            countList[i] += 1
        else:
            countList[i] = 1
    else:
        pass

sList = sorted(countList.items(),key=operator.itemgetter(1),reverse=True)
# print(sList)
# print(strList[0],currentRank)

for i in range(1,len(sList)):
    totalRank += 1
    if sList[i][1] ==sList[i-1][1] :
        pass
    else:
        currentRank = totalRank
    print(sList[i],currentRank)


##심화 : 단어##

countDic = {}

for data in strList2:
    if data[-1] =='.'or data[-1] ==',':                     #마침표와 쉼표를 떼어내는 코드
        data=data[:-1]
    if data[-1] in ['은','는','이','가','의','를','을','에']: #떼어낼 단어가 많을때 리스트를 사용
        data=data[:-1]
    if data in countDic :
        countDic[data] += 1
    else:
        countDic[data] = 1

print(countDic)
##db에서 자료를 불러올 때 ram에서 부하가 걸려서 느려지는 이슈가 있다.=>db에 대한 고려가 필요하다.














































































































