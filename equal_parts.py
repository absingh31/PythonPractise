def divide_equal(s, n):
	offset = int(len(s)/n)
	j=0
	for i in range(n):
		if(len(s)-j == offset+1):
			print(s[j:])
		else:
			print(s[j:j+offset])
		j = j+offset

if __name__=='__main__':
	divide_equal(input("Enter the string : "), int(input('How many parts you wanna divide in : ')))