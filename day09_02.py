import sqlite3
con = sqlite3.connect('userDB')             #데이터베이스 지정(또는 연결)
#sqlite3 는 본인 폴더에 있는 것을 접속하기 때문에 주소, 이름, 비번이 필요 없다.
cur =  con.cursor()                        #연결 통로 생성(쿼리문을 날릴 통로=cursor)

#테이블 만들기 (실무에서는 데이터베이스를 만들 일이 거의 없다.-없다고 보면 된다.)
#만들기는 두번 할 수 없다(중복이 되기 때문에) ==> 오류 : 예외처리가 필요한 이유
#try  구문에서 오류가 발생하면 except구문이 실행된다.
try :
    sql = "create table userTable(userID char(10), userName char(5), userAge int);"
    cur.execute(sql)                #sql문을 커서로 날려라
except :
    pass
while True :
    userID = input('아이디 -->')
    if userID == "":
        break
    userName = input('이름 -->')
    userAge = input('나이 -->')                               #: 쿼리문 날릴 때 문자열로 조합하기 때문에 str이 편하다.
    sql =  "insert into userTable(userID, userName, userAge)  values('"
    sql += userID +"','" + userName + "',"+userAge + ");"       #';'은 없어도 괜찮다.
    print('sql')





#
# sql = "insert into userTable values('AAA','에이',21);"
# cur.execute(sql)
# sql = "insert into userTable values('BBB',' 비이',23);"
# cur.execute(sql)
# sql = "insert into userTable values('CCC','씨이',35);"
# cur.execute(sql)
# # sql = "insert into userTable values('AAA','에이',21);"
# # cur.execute(sql)









cur.close()
con.close() #데이터베이스 연결 종료

print('ok')                     # 정상적으로 실행이 되었는지 확인







































































































