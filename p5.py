
num = 1
flag = 0

for i in range(2, 21):
	for j in range(2, i):
		if i % j == 0:
			flag = 1
			break
	if flag == 0:
		print i
		num = num * i
	flag = 0

print num * 24	
