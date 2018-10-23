#raw-->csv

import os
import math
import csv
import random

input_file ='D:\\data_analysis\\Pet_RAW\\Pet_RAW(64x64)\\cat02_64.raw'
output_file = 'D:\\data_analysis\\Pet_RAW\\Pet_RAW(64x64)\\cat02_64_2.csv'

header = ['Column', 'Row','Value']

rowFileList = []

with open(input_file,'rb') as filereader :
    with open(output_file,'w', newline="") as filewriter :
        csvWriter = csv.writer(filewriter)
        csvWriter.writerow(header)
        fsize = os.path.getsize(input_file)
        Xsize = Ysize = int(math.sqrt(fsize))
        for row in range(Xsize):
            for col in range(Ysize):
                data = int(ord(filereader.read(1)))
                row_list = [col,row,data]                       #화면과 실제는 x-y역전이 있다.
                rowFileList.append(row_list)

        random.shuffle(rowFileList)
        for row_list in rowFileList:
             csvWriter.writerow(row_list)

