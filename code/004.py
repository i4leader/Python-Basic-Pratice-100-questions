#!/usr/bin/python3

year = int(input("请输入年:"))
month = int(input("请输入月份:"))
day = int(input("请输入几号:"))

leapyear = [0,31,29,31,30,31,30,31,31,30,31,30,31]
normalyear = [0,31,28,31,30,31,30,31,31,30,31,30,31]

days = 0
i = month

if year%4 == 0:
    for temp in range(0,i,1):
        days += leapyear[temp]
    print("今年是闰年, ",end="")
else:
    for temp in range(0,i,1):
        days +=  normalyear[temp]

days = days + day
print('这是这一年的第%d天'%days)
