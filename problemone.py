import math
import time
print("calculating divisible numbers...")
divisible_num = []
for i in range(1,1001):
    if i%5 == 0 or i%3 == 0:
        divisible_num.append(i)
time.sleep(4)
print divisible_num
time.sleep(1)
print("Calculating sum...")
answer =sum(divisible_num)
time.sleep(3)
print("Done!")
time.sleep(1)
print answer

    




