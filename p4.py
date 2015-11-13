k = 0
flag = 0
max_num = 0

for i in range(999,99,-1):
	for j in range(999,99,-1):

		num = i * j

		while num / (10 ** k) != 0:
			k += 1
		
		for z in range(1, k/2 + 1):
			if (num / (10 ** (k - z))) % 10 != (num % (10 ** z)) /   (10 ** (z - 1)):
				flag = 1
				break
		
		if flag == 0:
			if max_num < num:
				max_num = num

		flag = 0
		k = 0

print max_num
