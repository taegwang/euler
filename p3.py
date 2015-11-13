import math

num = 600851475143
limit = int(math.sqrt(num))
flag = 0
i = limit

while i != 0:
	if num % i == 0:
		for j in range(2,i-1):
			if i % j == 0:
				flag = 1
				break
		if flag == 0:
			print i
			break 
		flag = 0
	i -= 1

