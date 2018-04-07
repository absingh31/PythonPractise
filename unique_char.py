
s = input('Enter the string : ')

def check_unique(s):
	for x in s:
		if(s.count(x)>1):
			return False
	return True


x = check_unique(s);
if(x==0):
	print("Not unique")
else:
	print("unique")