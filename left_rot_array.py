def left_rotate(k, *args):
	b = [x for x in args]
	left_b = [b[(k+i)%len(b)] for i in range(0,len(b))]
	return left_b

if __name__ == '__main__':
	arr = [int(x) for x in input('Enter the array elements').split()]
	k = input('Enter the value around which you wanna rotate')
	a = left_rotate(int(k), *arr)
	print(a)

