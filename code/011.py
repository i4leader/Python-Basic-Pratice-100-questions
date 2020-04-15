#!/usr/bin/python3

def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        a, b = b, (a+b)
    print("%d个月,小兔子数量为%d. "%(num,a*2))

num = int(input("请输入月份:"))
fibo(num)