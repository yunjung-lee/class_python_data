###CSV  안에 comma를 포함한 문자열이 있을 때 문자열은 상관없이 분리하는 방법

import csv

a='1234,John Smith,100-0014,"$1,350.00",3/4/14'
for a in  csv.reader([a],skipinitialspace=True):
    print(a)


