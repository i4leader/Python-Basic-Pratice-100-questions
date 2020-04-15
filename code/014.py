#!/usr/bin/python3

n=int(input('请输入一个整数:'))
n1=n
l=[]
while n>1:
    for i in range(2,int(n+1)):
        if n%i==0:
            n=n/i
            l.append(str(i))
            break

print('%d=' %n1 + '*'.join(l))



