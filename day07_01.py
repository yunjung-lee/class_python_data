#JSON 데이터도 처리하기.
#JSON 읽기 라이브러리 사용(딕셔너리 형태로 출력)

import json

jsonDic = {}
jsonList = []
csvList = []

filereader = open('TEST01.json', 'r', encoding='utf-8')

jsonDic = json.load(filereader)
csvName = jsonDic.keys()
# dict_keys(['userTable'])
csvName = list(jsonDic.keys())                          #딕셔너리를 리스트로 만들어줌
#['userTable']
#jsonList = list(jsonDic.values())[0]                   #아래와 같은 결과
jsonList = jsonDic[csvName[0]]
# [{'ID': 'AAA', 'NAME': '에이', 'ADDR': '서울'}, {'ID': 'BBB', 'NAME': '삐이', 'ADDR': '경기'}, {'ID': 'CCC', 'NAME': '씨이', 'ADDR': '강원'}]



#헤더리스트 추출
header_list = list(jsonList[0].keys())
csvList.append(header_list)
#행들 추출: 각 딕셔너리의 값으로 행을 만듬(딕셔너리는 순서가 없기 때문에 values로 행을 추출하면 안된다: 차례가 틀릴 수 있다.)
for tmpDic in jsonList:
    tmpList = []
    for header in header_list:
        data = tmpDic[header]                           #딕셔너리의 키에 해당하는 데이터를 data에 넣어준다: 왜??????
        tmpList.append(data)
    csvList.append(tmpList)

print(csvList)

filereader.close()