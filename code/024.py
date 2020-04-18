#!/usr/bin/python3

a = 1
b = 2
c = b/a
print("a=%d, b=%d, c=%f"%(a,b,c))
for i in range(19):
    a, b = b, (a+b)
    c += b/a
    print("a=%d, b=%d, c=%f"%(a,b,c))

