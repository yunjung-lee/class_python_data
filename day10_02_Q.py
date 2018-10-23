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


con = sqlite3.connect('c:/temp/userDB')  # 데이터베이스 지정(또는 연결)

cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

input_file = askdirectory()

sql = "SELECT name FROM sqlite_master WHERE type='table'"

cur.execute(sql)

cNameList = []

while True:

    row = cur.fetchone()

    if row == None:
        break

    cNameList.append(row[0])
    for name in cNameList:
        fileName = input_file+'/'+name+'.csv'
        print(fileName)
        filewriter = open(fileName,'w', newline='')
        csvWrite = csv.writer(filewriter)


        sql = "SELECT * FROM " + name
        cur.execute(sql)

        while True:

            row = cur.fetchone()


            if row == None:

                break

            for ii in range(1,len(row)) :

                cNameList.append(str(row[ii]))
                data_list = ','.join(cNameList)
            print(data_list)
            csvWrite.writerow(data_list + '\n')



    filewriter.close()
    print(fileName + ' 생성.')

cur.close()
con.close()
print('ok')






































































































