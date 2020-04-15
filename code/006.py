#!/usr/bin/python3

def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        a, b = b, (a+b)
        print(a,end=" ")

num = int(input("请输入您想显示的斐波那契数列个数:"))
fibo(num)