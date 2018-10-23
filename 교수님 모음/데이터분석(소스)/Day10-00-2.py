## 여러개의 대용량 CSV 파일 --> SQLite
from  tkinter import *
from  tkinter.simpledialog import *
from tkinter.filedialog import *
import csv
import glob
import os
import json
import os.path
import xlrd
import xlwt
import sqlite3
import pymysql

con = sqlite3.connect('c:/temp/userDB')  # 데이터베이스 지정(또는 연결)
cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

dirName = askdirectory()
# 폴더에서 *.csv 파일 목록만 뽑기

file_list = glob.glob(os.path.join(dirName, "*.csv"))
for input_file in file_list:
    filereader = open(input_file, 'r', newline='')
    csvReader = csv.reader(filereader)  # CSV 전용으로 열기
    colList = next(csvReader)
    tableName = os.path.basename(input_file).split(".")[0]
    print(tableName)
    try:
        sql = "CREATE TABLE " + tableName + "("
        for colName in colList :
            colNameList = colName.split()
            colName = ""
            for col in colNameList :
                colName += col
            sql += colName + " CHAR(20),"
        sql = sql[:-1]
        sql += ")"
        print(sql)
        cur.execute(sql)
    except:
        pass

    rowCount = 0
    for rowList in csvReader:
        sql = "INSERT INTO " + tableName + " VALUES("
        for row in rowList:
            sql += "'" + row + "',"
        sql = sql[:-1]
        sql += ")"
        cur.execute(sql)

    filereader.close()

con.commit()

cur.close()
con.close()