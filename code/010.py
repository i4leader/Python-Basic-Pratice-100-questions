# !/usr/bin/python3

import time

# 格式化成2020-04-15 15:20:48形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Wed Apr 15 15:20:48 2020形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Wed Apr 15 15:20:48 2020"
print (time.mktime(time.strptime(a ,"%a %b %d %H:%M:%S %Y")))