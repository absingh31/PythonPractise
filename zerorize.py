def zerorise(mat):
	for i in range(len(mat)):
		for j in range(len(mat[0])):
			if(mat[i][j]==0):
				flag_i = i
				flag_j = j

	for z in range(len(mat[0])):
		mat[flag_i][z] = 0
	for z in range(len(mat)):
		mat[z][flag_j] = 0

def print_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = ' ')
        print('\n')

if __name__ == "__main__":
	mat = [[1,2,3],[4,5,6],[7,0,9]]
	zerorise(mat)
	print_mat(mat)