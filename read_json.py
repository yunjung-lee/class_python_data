
# JSON 데이터도 처리하기.

import json

jsonDic = {}

jsonList = []

csvList = []




filereader = open('TEST01.json', 'r', encoding='utf-8')

jsonDic = json.load(filereader)

csvName = list(jsonDic.keys())

jsonList = jsonDic[ csvName[0]]

# 헤더 추출

header_list = list(jsonList[0].keys())

csvList.append(header_list)

# 행들 추출

for  tmpDic in jsonList :

    tmpList = []

    for  header in  header_list :

        data = tmpDic[header]

        tmpList.append(data)

    csvList.append(tmpList)

print(csvList)




filereader.close()
