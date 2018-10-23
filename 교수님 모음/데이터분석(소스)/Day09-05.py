# MySQL 접속하기.
import pymysql
# con = pymysql.connect(host='192.168.174.128', user='biguser',
#                       password='1234', db='userDB', charset='utf8')  # 데이터베이스 지정(또는 연결)
con = pymysql.connect(host='192.168.174.129', user='root',
                      password='1234', db='userDB', charset='utf8')  # 데이터베이스 지정(또는 연결)

cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

# 테이블 만들기
try :
    sql = "CREATE TABLE userTable2(userID CHAR(10), userName CHAR(5), userAge INT)"
    cur.execute(sql)
except :
    pass

sql = "INSERT INTO userTable2 VALUES('GGG', N'한글', 21);"
cur.execute(sql)
sql = "INSERT INTO userTable2 VALUES('NNN','DDD', 23);"
cur.execute(sql)
sql = "INSERT INTO userTable2 VALUES('YYY','CCC', 35);"
cur.execute(sql)

con.commit()

cur.close()
con.close() # 데이터베이스 연결 종료
print('Ok!')