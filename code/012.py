#!/usr/bin/python3
import math
count = 0
leap = 1

for i in range(101,201):
    k = int(math.sqrt(i+1))
    for j in range(2,k+1):
        if i%j == 0:
            leap = 0
            break
    if leap == 1:
        print(i)
        count += 1
    leap = 1

print("素数总计数:%d"%count)
