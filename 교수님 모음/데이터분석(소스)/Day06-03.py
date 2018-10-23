input_file = "d:\\pydata\\csv\\supplier_data.csv"
output_file = "d:\\pydata\\output\\result03.csv"

with open(input_file, 'r', newline='') as filereader :
    with open(output_file, 'w', newline='') as filewriter :

        header = filereader.readline()
        header  = header.strip() # 앞뒤 공백제거
        header_list = header.split(',')
        # 리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.
        header_str = ','.join(map(str, header_list))
        filewriter.write(header_str + '\n')
        for  row  in  filereader :  # 모든행은 row에 넣고 돌리기.
            row = row.strip()
            row_list = row.split(',')
            cost = float(row_list[3][1:])
            cost += 100
            cost_str = "${0:.2f}".format(cost)
            row_list[3] = cost_str
            row_str = ','.join(map(str, row_list))
            print(row_str)
            filewriter.write(row_str + '\n')

        print('Ok~~')