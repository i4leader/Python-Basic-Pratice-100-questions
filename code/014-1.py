
def run(num):
	n = num
	result = []
	for j in range(int(n/2)+1):
		for i in range(2,n):
			if num % i == 0:  #可以整除
				result.append(i)
				num = num // i
				break
	if len(result) == 0:
		print("此数是是质数，请重新输入另一个数")
		exit()
	#print(result)
	print('%d = '%(n),end='')
	for i in range(len(result)):
		if i  == len(result)-1:
			print('%s' % (result[i]))
		else:
			print('%s * ' % (result[i]),end='')


run(90)
