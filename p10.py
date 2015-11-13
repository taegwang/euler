import math

num = 0
flag = 0

for i in range(2, 2000000):
	for j in range(2,int(math.sqrt(i))+1):
		if i % j == 0:
			flag = 1
			break
	if flag == 0:
		num += i
	flag = 0

print num	
