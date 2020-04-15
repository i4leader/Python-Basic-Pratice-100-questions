#!/usr/bin/python3
s1 = "+"
list2 = []
list3 = []
for x in range(1, 1001):
    list1 = []
    list3 = []
    for i in range(1, int(x / 2) + 1):
        if x % i == 0:
            list3.append(i)
            i = str(i)
            list1.append(i)
    if x == sum(list3):
        print("%d = "%x, end="")
        print(s1.join(list1))

        list2.append(x)
print("共计有%d个完数"%(len(list2)))