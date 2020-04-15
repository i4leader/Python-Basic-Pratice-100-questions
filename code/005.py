#!/usr/bin/python3

x = int(input("请输入数字1:"))
y = int(input("请输入数字2:"))
z = int(input("请输入数字3:"))

listA = [x,y,z]
# 方法一
print(listA)
listA.sort()
print(listA)

# 方法二
i=0
while i<3:
    print(listA[i],end=" ")
    i+=1
print("")