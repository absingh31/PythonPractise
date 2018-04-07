def max_occurance(s):
	d = {}
	for i in s:
		if i in d:
			d[i]+=1
		else:
			d[i] = 1

	return max(d.items(), key = lambda x : x[1]) 

if __name__ == '__main__':
	print(max_occurance(input("Enter the string : ")))