#!/usr/bin/python3

for num in range(100,1000):
    # 方法一
    strnum = str(num)
    i = int(strnum[0])
    j = int(strnum[1])
    k = int(strnum[2])
    if i*i*i + j*j*j + k*k*k == num:
        print(num)

    # 方法二
    i = int(num/100)
    j = int(num/10%10)
    k = num%10
    if num == i ** 3 + j ** 3 + k ** 3:
        print(num)