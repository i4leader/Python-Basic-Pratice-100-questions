#!/usr/bin/python3

import datetime

# 返回当前系统时间
print(datetime.datetime.now())

# 日期格式转化为字符串格式
print(datetime.datetime.now().strftime('%b-%d-%Y %H:%M:%S'))

# 打印指定日期
print(datetime.datetime(2020,4,24))