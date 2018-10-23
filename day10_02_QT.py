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


con = sqlite3.connect('c:/temp/userDB')

cur = con.cursor()




    # 저장할 폴더 선택하기.

dirName = askdirectory()




    # 각 테이블을 CSV로 저장하기. (테이블당 파일 1개)

sql = "SELECT name FROM sqlite_master WHERE type='table'"

cur.execute(sql)

tableNameList = []

while True:

    row = cur.fetchone()

    if row == None:

        break

    tableNameList.append(row[0]);




    # 각 파일을 SQLite에 저장하기. (파일당 테이블 1개)

for tableName in tableNameList:

    output_file =  dirName + '/' + tableName + '.csv'

    filewriter = open(output_file, 'w', newline='')

    csvWrite = csv.writer(filewriter)




        # 열이름 추출

        # 테이블의 열 목록 뽑기

    sql = "SELECT * FROM " + tableName

    cursor = con.execute(sql)

    colNameList = list(map(lambda x: x[0], cursor.description))
    print(colNameList)
    csvWrite.writerow(colNameList)




        # CSV에 행 데이터 쓰기

    sql = "SELECT * FROM " + tableName

    cur.execute(sql)

    while True:

        row = cur.fetchone()

        if row == None:

            break

        row_list = []

        for ii in range(len(row)):
            row_list.append(row[ii])


        print(row_list)

        csvWrite.writerow(row_list)




    filewriter.close()

    print(output_file + ' 생성.')




cur.close()

con.close()

print("OK!")














































































