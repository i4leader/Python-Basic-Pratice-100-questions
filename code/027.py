#!/usr/bin/python3

def output(string,length):
    if length == 0:
        return
    print(string[-1],end="")
    string = string[0:-1]
    output(string,length-1)

strA = input("请输入一串字符:")
l = len(strA)
output(strA,l)
