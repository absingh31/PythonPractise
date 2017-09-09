def check_bit_rotation(a, b):
	while(a>=b):
		if a==b :
			print("Yo! they're bit rotation of each other")
			break
		
		if a==1 :
			print("It's what you think!")
		a=a>>1		
	
		

if __name__ == '__main__':
	n_arr = [int(x) for x in input('Enter the 2 numbers\n').split()]
	check_bit_rotation(max(n_arr), min(n_arr))

