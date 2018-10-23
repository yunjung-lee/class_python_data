# SQLite 접속하기.
import sqlite3
con = sqlite3.connect('c:/temp/userDB')  # 데이터베이스 지정(또는 연결)
cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)
# 테이블 만들기
try :
    sql = "CREATE TABLE userTable(userID CHAR(10), userName CHAR(5), userAge INT)"
    cur.execute(sql)
except :
    pass

sql = "INSERT INTO userTable VALUES('GGG','에이', 21);"
cur.execute(sql)
sql = "INSERT INTO userTable VALUES('NNN','삐이', 23);"
cur.execute(sql)
sql = "INSERT INTO userTable VALUES('YYY','씨이', 35);"
cur.execute(sql)

con.commit()

cur.close()
con.close() # 데이터베이스 연결 종료
print('Ok!')