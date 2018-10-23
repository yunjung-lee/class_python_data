# 복습퀴즈2. 구구단을 처리하되, 각 결과의 앞자리~뒷자리까지 합계로 출력한다.
#    예)  2x1=3   (값2를 02로 취급해서 0부터 2까지의 합계 : 0+1+2 = 3)
#          2x2=10 (값2를 02로 취급해서 0부터 2까지의 합계 : 0+1+2+3+4 = 10)
#          ...
#          2x9=36  (값18을 1부터 8까지 : 1+2+3+4+5+6+7+8=36)
#          ...
#          8x8=15  (값64를 6부터 4까지 : 6+5+4 = 15)

for i  in  range(2, 10) :
    print('##', i, '단##')
    for k  in range(1, 10) :
        res = i*k
        if res < 10 :
            start = 0
        else :
            start = int(res / 10)
        end = res % 10
        if start > end :
            start, end = end, start

        hap = 0
        for num in range(start, end+1) :
            hap += num

        print(i, 'x', k, '=', hap)
    print('\n')