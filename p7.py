count = 0
num = 2
flag = 0

while count != 10001:
	for i in range(2,num):
		if num % i == 0:
			flag = 1
			break
	
	if flag == 0:
		print num
		count += 1

	flag = 0
	num += 1		
