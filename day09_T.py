# (1) 통계 기반 데이터 분석 (부제: 영상 처리를 통한 데이터 분석 및 통계 처리)
#
# (2) 텍스트마이닝 기반 데이터 분석 (부제: 텍스트 기반 데이터 분석 및 처리)
#
# (3) 빅데이터 분석 결과 시각화 (부제 : 데이터베이스 기반 데이터 분석 및 GUI 시각화)
#
#
#
#
#
#
#
# 복습퀴즈1. MySQL에서 다음과 같이 작업하시오.
#
#
#
#
#  (1) 사용자 생성 : 자신 이름 영문 약자 (예:홍길동은 hongUser/hong1234)
#
#
#
#
#  (2) 데이터베이스 생성 : 자신 이름 영문 약자 (예:홍길동은 hongDB)
#
#
#
#
#  (3) 사원테이블(사번, 이름, 직급, 입사년도, 월급여) 생성
#
#
#
#
#  (4) 데이터를 적당히 3건 입력 --> 영문으로 입력
#
#
#
#
#
#
#
# 복습퀴즈2. GUI 툴에 메뉴 추가하기. (카페에서 마지막 버전 사용)
# 
#
#
#
#    [MySQL 데이터 분석] - [MySQL 정보읽기] 및 [MySQL 정보쓰기]


import pymysql
con = pymysql.connect(host = '192.168.93.128',user = 'biguser',password = '1234', db = 'userDB')            #데이터베이스 지정(또는 연결)
cur =  con.cursor()                        #연결 통로 생성(쿼리문을 날릴 통로=cursor)


sql = "select * from userTable2"
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







































































































