
# SQLite 접속하기.

import sqlite3

con = sqlite3.connect('userDB')  # 데이터베이스 지정(또는 연결)

cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

# 테이블 만들기

try :

    sql = "CREATE TABLE userTable(userID CHAR(10), userName CHAR(5), userAge INT);"

    cur.execute(sql)

except :

    pass




while True :

    userID = input('아이디-->')

    if userID == "" :

        break

    userName = input('이름-->')

    userAge = input('나이-->')

    sql = "INSERT INTO userTable(userID, userAge, userName ) VALUES('"

    sql += userID + "',"+ userAge + ",'" + userName + "')"

    cur.execute(sql)




cur.close()

con.close() # 데이터베이스 연결 종료

print('Ok!')
