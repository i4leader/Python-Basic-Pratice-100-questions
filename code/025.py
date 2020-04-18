#!/usr/bin/python3

def factorial(num):
    result1 = 1
    resultsum = 0
    for i in range(1,num+1):
        result1 *= i
        resultsum += result1
    return resultsum

print(factorial(20))
