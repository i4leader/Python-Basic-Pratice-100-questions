#!/usr/bin/python3

intlist = [1,2,3,4]
for i in intlist:
    for j in intlist:
        for k in intlist:
            if i != j and j != k and i!= k:
                print(i,j,k)