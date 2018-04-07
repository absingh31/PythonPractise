def pallin(s,a):
	if(a==s[::-1]):
		print("Pallindrome")
	else:
		print("Not Pallindrome")

def anagram(s,a):
	a_=sorted(a)
	s_=sorted(s)
	if(s_==a_):
		print("Anagram")
	else:
		print("Not Anagram")

if __name__=="__main__":
	x = input("Enter the first string : ")
	y = input("Enter the second string : ")
	pallin(x,y)
	anagram(x,y)