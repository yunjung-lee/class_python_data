
input_file = "d:\\data_analysis\\csv\\supplier_data.csv"
output_file = "d:\\data_analysis\\output\\result03.csv"


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
        #리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.=>csv로 저장하기 위해서
        #map = 리스트로 (a,b) a형식으로 b를 하나하나 만들어준다.
        #header_str = map(str,header_list)
        header_str = ','.join(map(str,header_list))
        filewriter.write(header_str+'\n')
        #모든 행을 row에 넣고 돌리기.
        for row in filereader :
           row=row.strip()
           row_list = row.split(',')
           #cost를 100더한 값
           #내가 한것
           # row_list[3]=row_list[3][:-6]+str(int(row_list[3][-6])+1)+row_list[3][-5:0]

           #교수님께서 한것
           cost = float(row_list[3][1:])
           cost +=100
           cost_str = "${0:.2f}".format(cost)

           row_list[3] = cost_str
           row_str = ','.join(map(str,row_list))
           # print(row_list)
           filewriter.write(row_str+'\n')



           print(row_list)



print('ok')



