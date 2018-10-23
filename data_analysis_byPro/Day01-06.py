# 로또(lotto) 추첨 프로그램.
import random

lotto = []  # 45  -->  6

while True:
    num = random.randint(1,45)
    if lotto.count(num) > 0 :
        continue
    lotto.append(num)
    if len(lotto) >= 6 :
        break
        
lotto.sort()
print(lotto)
