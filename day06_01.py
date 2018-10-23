#!/usr/bin/env python3 :  없어도 문제는 없지만 (윈도우에서는 상관없지만 유닉스에선 python3인식)
import sys  #명령창과 연결하는 기능

#명령프롬프트 창에서 입출력
#D:\data_analysis>d:\ana\python day06_01.py  "d:\data_analysis\csv\supplier_data.csv" "d:\data_analysis\output"
#순서 : 파이썬 경로_sys가 있는 파일 이름(파일이 있는 디렉토리에서 실행)_"자료이름 및 경로"_"출력경로"

#실행 내용(명령프롬프트창)
# D:\data_analysis>d:\ana\python day06_01.py "d:\data_analysis\csv\supplier_data.csv" "d:\data_analysis\output"
# d:\data_analysis\csv\supplier_data.csv d:\data_analysis\output

#명령창 :  python Day06_01.py[0] 파라미터1[1] 파리미터2[2] .......

input_file = sys.argv[1]
output_file = sys.argv[2]


#많이 쓰는 변수 filereader
filereader = open(input_file,'r',newline='')
filewriter =  open(input_file,'w',newline='')

header = filereader.readline()
print(input_file,output_file)

filereader.close()
filewriter.close()




