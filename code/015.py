#!/usr/bin/python3

def grade(num):
    if num >= 90:
        return "A"
    elif num >= 60:
        return "B"
    else:
        return "C"

num = int(input('请输入学生的成绩:'))
print("该学生成绩为:%s"%(grade(num)))