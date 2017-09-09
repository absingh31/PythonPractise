def rotate(to_rotate):
	goin_to_rotate = [x for x in to_rotate]
	rotated = [goin_to_rotate[((k+i)%len(goin_to_rotate))] for i in range(len(goin_to_rotate))]
	rotated_word = ''.join(rotated)	
	return rotated_word

if __name__ == '__main__':
	word = input('Enter the word \n')
	for k in range(1,len(word)+1):
		x = rotate(word)
		if x == word :
			print(k)
			break
