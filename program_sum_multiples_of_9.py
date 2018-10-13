
#program to print the sum of multiples of nine between 1 and 250
sum = 0
for i in range(1,250):
	if (i%9 == 0):
		sum=sum+i
print(sum)
