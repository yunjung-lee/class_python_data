import math
input_file = "d:\\data_analysis\\csv\\supplier_data.csv"
output_file = "d:\\data_analysis\\output\\result04.csv"


#많이 쓰는 변수 filereader
with open(input_file,'r',newline='') as filereader :
    with open(output_file,'w',newline='') as filewriter :

#with절이 깔끔함 close가 없어도 되서

        #input과 output을 동일하게
        header = filereader.readline()
        #앞뒤 공백 제거
        header = header.strip()
        #문자별로 분리
        header_list = header.split(',')
        #part number, purchase date 열을 지우기

        #
        # # idx1 = 0
        # # for h in header_list :
        # #     if h.strip().upper() == 'part Number'.strip().upper():          #대소문자 비교& 앞뒤 공백 제거
        # #         break
        # #     idx1 += 1
        # # idx2 = 0
        # # for h in header_list:
        # #    if h.strip().upper() == 'part Number'.strip().upper():  # 대소문자 비교& 앞뒤 공백 제거
        # #        break
        # # idx2 += 1
        # # if idx1 > idx2:
        # #     idx1,idx2=idx2,idx1
        #
        header_str = ','.join(map(str,header_list))
        filewriter.write(header_str+'\n')
        #모든 행을 row에 넣고 돌리기.

#퀴즈 3 조건1)열중에서 part number와 putchase data는 제거한다.
#      조건 2) supplier Y행은 지운다.
#      조건 3) 가격을 모두 1.5배 인상시킨다.
#           그리고 100달러 미만 단위는 버린다.770->700
        for row in filereader :
           row=row.strip()
           row_list = row.split(',')
           row_list.pop()
           del row_list[2]
           # del row_list[idx2]
           # del row_list[idx1]
           if row_list[0]=='Supplier Y':
               continue
           cost = float(row_list[2][1:])
           cost *1.5
           cost = math.floor(cost/100)*100
           cost_str = "${0:.2f}".format(cost)
           row_list[2] = cost_str
           row_str = ','.join(map(str,row_list))
           filewriter.write(row_str+'\n')



           print(row_list)



print('ok')



