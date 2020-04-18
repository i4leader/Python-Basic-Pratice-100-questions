#!/usr/bin/python3

i = 3
j = 1
while i > 0 or j < 8:
    print(" " * i, end="")
    print("*" * j)
    i -= 1
    j += 2
if i <= 0:
    m = 1
    n = 5
    while m < 3 or n> 0:
        print(" " * m,end="")
        print("*" * n)
        m += 1
        n -= 2
