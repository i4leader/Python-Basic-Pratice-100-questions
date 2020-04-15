#!/usr/bin/python3

strA = input("请输入一串字符串:")

number = 0
space = 0
alpha = 0
other = 0

for i in strA:
    if i.isnumeric() == True:
        number += 1
    elif i.isspace() == True:
        space += 1
    elif i.isalpha() == True:
        alpha += 1
    else:
        other += 1
print('本字符串总长度为:%d'%(len(strA)))
print("字符串中字母有%d个,数字有%d个,空格有%d个,其他字符有%d个"%(alpha, number, space, other))