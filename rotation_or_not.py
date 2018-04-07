def check_rotation(s,a):
	sa = s+s
	if(sa.count(s)>0 and sa.count(a)>0):
		print("Rotation hai bhai")
	else:
		print("Nope!!! sorry, rotation nhi hai")


if __name__=='__main__':
	check_rotation(input('Enter the first string : '), input('Enter the second string : '))