# SQLite 접속하기.
import sqlite3
con = sqlite3.connect('c:/temp/userDB')  # 데이터베이스 지정(또는 연결)
cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

sql = "SELECT * FROM userTable"
cur.execute(sql)

print(' 사용자아이디  사용자이름  사용자나이')
print(' --------------------------------')
while True :
    row = cur.fetchone()
    if row == None :
        break
    userID  = row[0]; userName = row[1]; userAge = row[2]
    print("%10s %10s  %10d" % (userID, userName, userAge))

cur.close()
con.close() # 데이터베이스 연결 종료
print('Ok!')