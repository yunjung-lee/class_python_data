#raw-->csv

import os
import math
import csv

input_file ='D:\\data_analysis\\Pet_RAW\\Pet_RAW(64x64)\\cat02_64.raw'
output_file = 'D:\\data_analysis\\Pet_RAW\\Pet_RAW(64x64)\\cat02_64.csv'

header = ['Column', 'Row','Value']


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
                csvWriter.writerow(row_list)

