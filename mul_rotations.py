def rotate(k, *arr):
	a = [int(x) for x in arr]
	b = [a[(k+i)%len(a)] for i in range(len(a))]
	return b


if __name__ == '__main__':
	arr = [int(x) for x in input('Enter the array elements').split()]
	
	for k in range(1, len(arr)):
		x = rotate(k, *arr)
		print(x)


