#!/usr/bin/python3

def fact(num):
    sum = 0
    if num == 0:
        sum = 1
    else:
        sum = num * fact(num - 1)
    return sum

print(fact(5))