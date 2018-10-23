import sqlite3
con = sqlite3.connect('userDB')             #데이터베이스 지정(또는 연결)
cur =  con.cursor()                        #연결 통로 생성(쿼리문을 날릴 통로=cursor)


sql = "select * from userTable"
cur.execute(sql)

print("사용자 아이디    사용자 이름   사용자나이")
print("_______________________________________")
while True :
    row = cur.fetchone()                             #하나씩 가져오는 명령어 모두 가져오면(fetchall) 메모리가 넘쳐서 안됨
    if row == None:
        break
    userID =  row[0]
    userName = row[1]
    userAge =  row[2]
    print("%10s, %10s, %10d" % (userID, userName, userAge))





cur.close()
con.close() #데이터베이스 연결 종료

print('ok')                     # 정상적으로 실행이 되었는지 확인







































































































