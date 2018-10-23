#!/usr/bin/env python3 :  없어도 문제는 없지만 (윈도우에서는 상관없지만 유닉스에선 python3인식)
import sys  #명령창과 연결하는 기능


#명령창 :  python Day06_01.py[0] 파라미터1[1] 파리미터2[2] .......

input_file = "d:\\data_analysis\\csv\\supplier_data.csv"
output_file = "d:\\data_analysis\\output\\result02.csv"


#많이 쓰는 변수 filereader
filereader = open(input_file,'r',newline='')
filewriter = open(output_file,'w',newline='')


#input과 output을 동일하게
header = filereader.readline()
#앞뒤 공백 제거
header = header.strip()
#문자별로 분리
header_list = header.split(',')
#리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.=>csv로 저장하기 위해서
#map = 리스트로 (a,b) a형식으로 b를 하나하나 만들어준다.
#header_str = map(str,header_list)
header_str = ','.join(map(str,header_list))
filewriter.write(header_str+'\n')
#모든 행을 row에 넣고 돌리기.
for row in filereader :
    row=row.strip()
    row_list = row.split(',')
    row_str = ','.join(map(str,row_list))
    print(row_list)
    filewriter.write(row_str+'\n')



print(header_str)




filereader.close()
filewriter.close()
print('ok')



