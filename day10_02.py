##여러개의 대용량 csv --> SQLite

from  tkinter import *

from  tkinter.simpledialog import *

from tkinter.filedialog import *

import csv

import json

import os

import os.path

import xlrd

import xlwt

import sqlite3

import pymysql

import glob




con  = sqlite3.connect('c:/temp/userDB')                #db가 없으면 만들어 넣는다.
cur = con.cursor()

#폴더 선택하고 그 안의 파일 목록들 추출하기
dirName = askdirectory()
file_list = glob.glob(os.path.join(dirName,'*.csv'))

#각 파일을  SQLite에 저장하기.(파일당 테이블 1개)
#울트라 에딧 :  메모장은 큰 용량을 소화하지 못하기 때문에 사용한다.
for input_file in file_list:
    filereader = open(input_file, 'r', newline="")
    csvReader = csv.reader(filereader)
    colList = next(csvReader)           #열이름들
    tableName = os.path.basename(input_file).split(".")[0]
    try:
        sql = "create table "+tableName+"("
        for colName in colList:
            cList = colName.split()
            colName = ""
            for col in cList:
                colName += col + '_'
            colName = colName[:-1]
            sql += colName+" char(20),"
        sql = sql[:-1]
        sql += ')'
        cur.execute(sql)
        print(sql)

    except :
        print("테이블 이상 --> ", input_file)
        continue   #자료 입력 없이 다음 파일로 넘어감

    for rowList in csvReader :
        sql = "insert into "+tableName+" values("
        for data in rowList:
            sql += "'"+data+"',"
        sql = sql[:-1] +')'
        cur.execute(sql)




    filereader.close()
    con.commit()




print(file_list)

cur.close()
con.close()
print('ok')






































































































