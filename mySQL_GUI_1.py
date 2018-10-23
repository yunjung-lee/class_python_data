
def mysqlData01() :

    con = pymysql.connect(host='192.168.174.129', user='root',

                          password='1234', db='userDB', charset='utf8')  # 데이터베이스 지정(또는 연결)

    cur = con.cursor()  # 연결 통로 생성 (쿼리문을 날릴 통로)

    csvList = []

    # 데이터베이스 내의 테이블 목록이 궁금?

    sql = "SHOW TABLES"

    cur.execute(sql)

    tableNameList = []

    while True :

        row = cur.fetchone()

        if row == None:

            break

        tableNameList.append(row[0]);




    ##################################

    def selectTable() :

        selectedIndex = listbox.curselection()[0]

        subWindow.destroy()

        # 테이블의 열 목록 뽑기

        colNameList = []

        sql = "DESC " + tableNameList[selectedIndex]

        cur.execute(sql)

        while True:

            row = cur.fetchone()

            if row == None:

                break

            colNameList.append(row[0]);




        csvList.append(colNameList)

        sql = "SELECT * FROM " + tableNameList[selectedIndex]

        cur.execute(sql)

        while True:

            row = cur.fetchone()

            if row == None:

                break

            row_list = []

            for ii in range(len(row)) :

                row_list.append(row[ii])




            csvList.append(row_list)




            drawSheet(csvList)




    subWindow = Toplevel(window)  # window의 하위로 지정

    listbox = Listbox(subWindow)

    button = Button(subWindow, text='선택', command=selectTable)

    listbox.pack(); button.pack()

    for  sName in tableNameList :

        listbox.insert(END, sName)

    subWindow.lift()




    ####################################
