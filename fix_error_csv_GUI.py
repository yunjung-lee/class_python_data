## GUI 툴에서 CSV 열기 및 저장 함수를 다음과 같이 변경하면 오류가 발생하지 않음.




def openCSV() :

    global  csvList, input_file

    csvList = []

    input_file = askopenfilename(parent=window,

                filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))

    filereader = open(input_file, 'r', newline='')

    csvReader = csv.reader(filereader) # CSV 전용으로 열기

    header_list = next(csvReader)

    csvList.append(header_list)

    for row_list in csvReader:  # 모든행은 row에 넣고 돌리기.

        csvList.append(row_list)




    drawSheet(csvList)

    filereader.close()







def  saveCSV() :

    global csvList, input_file

    if csvList == [] :

        return

    saveFp = asksaveasfile(parent=window, mode='w', defaultextension='.csv',

               filetypes=(("CSV파일", "*.csv"), ("모든파일", "*.*")))

    filewriter = open(saveFp.name, 'w', newline='')

    csvWrite = csv.writer(filewriter)

    for  row_list  in  csvList :

        csvWrite.writerow(row_list)




    filewriter.close()
