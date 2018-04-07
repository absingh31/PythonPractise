def max_profit(a):
	max_p = -1
	for i in range(len(a)):
		for j in range(i, len(a)):
			if(a[j]-a[i]>max_p):
				max_p = a[j]-a[i]
	print(max_p)

def max_profit_optimised(a):
	min_s = a[0]
	max_p = -1
	for i in a:
		if(i<min_s):
			min_s = i
		if(i-min_s > max_p):
			max_p = i-min_s

	print(max_p)

if __name__ == '__main__':
	max_profit_optimisedt([int(input("Enter the array element : ")) for i in range(int(input("Enter the size of the element : ")))])
