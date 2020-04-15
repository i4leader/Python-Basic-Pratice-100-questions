#!/usr/bin/python3

n = int(input('请输入数字:'))
a = n
sum = 0
total = 0
for i in range(n):
    sum += (10 ** i)
    total += sum * a
print(total)