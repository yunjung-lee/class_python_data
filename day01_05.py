#간단 구구단

# for i in range(2,10):
#     print('##', i ,'단','##')
#     for k in range(1,10):
#         print(i,'x',k,'=',i*k)
#     print('\n')
#

# 문제 :  나는 구구단을 몰라요.... 그런데, 50이 넘으면 집에 갈래요...
#swich : for 구문을 나오는데 다음 명령까지 모두 캔슬되는 명령

sw = False
for i in range(2,10):
    if sw :
        break
    print('##', i ,'단','##')
    for k in range(1,10):
        if i * k >= 50:
            sw=True
            break
        print(i, 'x', k, '=', i * k)
    print('\n')