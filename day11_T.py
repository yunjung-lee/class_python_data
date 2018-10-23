# (1) 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리)
#
# (2) 텍스트마이닝 기반 데이터 분석 (부제: 텍스트 기반 데이터 분석 및 처리)
#
# (3) 빅데이터 분석 결과 시각화 (부제 : 데이터베이스 기반 데이터 분석 및 GUI 시각화)

# 복습퀴즈1. 선택한 폴더의 모든 RAW 파일을 MySQL의 테이블(rawTable)로 입력되는
#               코드를 작성하세요. (별도의 소스코드에 작성)

#     --> 파일이 크면 느리므로, 64x64 파일 몇개를 적당한 폴더에 복사한 후 테스트

# 복습퀴즈2. MySQL 테이블(rawTable)의 모든 데이터가,
#            선택한 폴더의 RAW 파일로 저장되는 코드를 작성하세요.

import pymysql
from tkinter import  *
from tkinter.filedialog import *
import sys
import xlwt
import os.path
import math


input_file = askdirectory()
inFile = os.listdir(input_file)
inFile = inFile

con = pymysql.connect(host='192.168.93.131', user='root',password='1234', db='imageDB', charset='utf8')  # 데이터베이스 지정(또는 연결)
cur = con.cursor()


filename = 0
colList = []
for filename in inFile:
    filename = filename.split(".")[0]
    try:

        sql = "CREATE TABLE "+filename+"Table( filename CHAR(20), resolution smallint" + ", row  smallint,  col  smallint, value  smallint)"

        cur.execute(sql)
        print(filename)


    except:

        pass

with open(inFile, 'rb') as filereader:
    pass



con.commit()

cur.close()

con.close()  # 데이터베이스 연결 종료

print('Ok! saveMySQL')



