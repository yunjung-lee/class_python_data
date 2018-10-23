#엑셀의 시트처럼 보이는 것 만들기.
input_file = "d:\\data_analysis\\csv\\supplier_data.csv"
output_file = "d:\\data_analysis\\output\\result04.csv"

from tkinter import *


with open(input_file,'r',newline='') as filereader :
    with open(output_file,'w',newline='') as filewriter :

        header = filereader.readline()
        header = header.strip()
        header_list = header.split(',')
        header_str = ','.join(map(str, header_list))
        filewriter.write(header_str + '\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            row_str = ','.join(map(str, row_list))
            filewriter.write(row_str + '\n')
            csvList = []
            for i in range(len(header_str)):
                for row in range(len(filereader)):
                    csvList.append(row_str)
            print(csvList)

#
# # csvList = [['제목1','제목2','제목3'],
# #            [111, 222, 333],
# #            [444, 555, 666],
# #            [777, 888, 999]]             #csv에서 읽어온 값
# #
# window=Tk()
# # window.geometry('400x400')
# csvList = []
# # for i in range(len(row_list[0])):
# #     csvList.append(row_list)
#     # print(csvList)
# rowNum = len(row_list)
# colNum = len(row_list[0])
# cellList = []
# #빈 시트 만들기
# for i in range(0,rowNum):
#     tmpList = []
#     for k in range(0, colNum):
#         ent = Entry(window)
#         tmpList.append(ent)
#         ent.grid(row=i,column=k)
#     cellList.append(tmpList)
# #시트에 리스트값 채우기<=각 엔트리에 값넣기
# for i in range(0,rowNum):
#     for k in range(0,colNum):
#         cellList[i][k].insert(row_list[i],row_list)
#
#
# #
# #
# #
# window.mainloop()
# #
# #
































