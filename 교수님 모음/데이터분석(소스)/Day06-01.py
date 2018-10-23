#!/usr/bin/env  python3
import  sys  # 명령창과 연결하는 기능
# 명령창 :  python  Day06-01.py  파라미터1  파라미터2 ....
input_file =sys.argv[1]
output_file = sys.argv[2]

filereader = open(input_file, 'r', newline='')
filewriter = open(input_file, 'w', newline='')

header = filereader.readline()
print(header)



filereader.close()
filewriter.close()
