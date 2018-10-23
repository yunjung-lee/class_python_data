
import pymysql
con = pymysql.connect(host = '192.168.93.128',user = 'biguser',password = '1234', db = 'userDB')             #호스트번호(또는 연결번호)
cur =  con.cursor()                        #연결 통로 생성(쿼리문을 날릴 통로=cursor)


try :
    sql = "create table userTable2(userID char(10), userName char(5), userAge int);"
    cur.execute(sql)                #sql문을 커서로 날려라
except :
    pass

sql = "insert into userTable2 values('AAA','aaa',21);"
cur.execute(sql)
sql = "insert into userTable2 values('BBB','bbb',23);"
cur.execute(sql)
sql = "insert into userTable2 values('CCC','ccc',35);"
cur.execute(sql)

con.commit()






cur.close()
con.close() #데이터베이스 연결 종료

print('ok')