def check_occurance(s):
	for x in s:
		if(s.count(x)==1):
			print(x)
			break

if __name__=="__main__":
	check_occurance(input("Enter the string : "))