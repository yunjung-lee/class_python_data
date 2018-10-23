# 퀴즈3. result03.csv에 출력

#          조건1. 5개 열 중에서 part Number와 Purchase Date는 제거한다.

#          조건2. Supplier Y 행은 지운다.

#          조건3. 가격을 모두 1.5배 인상시킨다.

#                    그리고, 100달러 미만 단위는 버린다.  770 --> 700

#

# 심화퀴즈3.  열이 굉장히 많다고 가정해서 part Number와 Purchase Date의

#  위치를 모른다.







input_file = "d:\\data_analysis\\csv\\supplier_data.csv"
output_file = "d:\\data_analysis\\output\\result04.csv"




with open(input_file, 'r', newline='') as filereader :

    with open(output_file, 'w', newline='') as filewriter :




        header = filereader.readline()

        header  = header.strip() # 앞뒤 공백제거

        header_list = header.split(',')

        # part Number, Purchase Date

        idx1 = 0

        for h in header_list :

            if h.strip().upper() == 'part Number'.strip().upper() :

                break

            idx1 += 1

        idx2 = 0

        for h in header_list :

            if h.strip().upper() == 'Purchase Date'.strip().upper() :

                break

            idx2 += 1

        if idx1 > idx2 :

            idx1, idx2 = idx2, idx1

        # 리스트를 다시 콤마(,)로 분리된 문자열로 만들고 싶다.

        header_str = ','.join(map(str, header_list))

        filewriter.write(header_str + '\n')

        for  row  in  filereader :  # 모든행은 row에 넣고 돌리기.

            row = row.strip()

            row_list = row.split(',')

            del(row_list[idx2])

            del(row_list[idx1])

            if row_list[0] == 'Supplier Y' :

                continue

            cost = float(row_list[2][1:])

            cost *= 1.5

            cost = int(cost/100) * 100

            cost_str = "${0:.2f}".format(cost)

            row_list[2] = cost_str

            row_str = ','.join(map(str, row_list))

            print(row_str)

            filewriter.write(row_str + '\n')




        print('Ok~~')