#!/usr/bin/python3

def bounce(num):
    global a
    height = 100
    listHeight = []
    for i in range(1,num+1):
        height /= 2
        listHeight.append(height)
        a = (sum(listHeight) - listHeight[-1])*2 + 100

    print("本次反弹%f米."%height)
    print("总计经过%f米."%(a))

bounce(10)