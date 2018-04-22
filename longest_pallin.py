def check_pallin(s):
	if(s == s[::-1]):
		return True
	return False

def finf_longest_pallin(s):
	aux = ""
	d = {"string":0}
	for i in s:
		aux = aux + i
		if(len(aux)>0 and check_pallin(aux)):
			d[aux] = len(aux)
	#print(d)
	return max(d.items(), key = lambda x : x[1])


if __name__ == '__main__':
	print(finf_longest_pallin(input("Enter the string : ")))