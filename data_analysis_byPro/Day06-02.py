#!/usr/bin/env  python3
import  sys  # 명령창과 연결하는 기능
# 명령창 :  python  Day06-01.py  파라미터1  파라미터2 ....
input_file = "d:\\pydata\\csv\\supplier_data.csv"
output_file = "d:\\pydata\\output\\result02.csv"

filereader = open(input_file, 'r', newline='')
filewriter = open(output_file, 'w', newline='')

header = filereader.readline()
header  = header.strip() # 앞뒤 공백제거
header_list = header.split(',')
# 리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.
header_str = ','.join(map(str, header_list))
filewriter.write(header_str + '\n')
for  row  in  filereader :  # 모든행은 row에 넣고 돌리기.
    row = row.strip()
    row_list = row.split(',')
    row_str = ','.join(map(str, row_list))
    print(row_str)
    filewriter.write(row_str + '\n')

filereader.close()
filewriter.close()
print('Ok~~')