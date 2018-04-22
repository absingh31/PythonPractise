def clock_ninety(mat, r, c):
    #first we find the transpose
    for i in range(r):
        for j in range(i,c):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    #reverse the column
    for i in range(int((c+1)/2)):
        mat[i][j], mat[i][c-1-j] = mat[i][c-1-j], mat[i][j]

def anticlock_ninety(mat, r, c):
    #first we find the transpose
    for i in range(r):
        for j in range(i,c):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    #reverse the column
    for i in range(int((r+1)/2)):
        mat[i][j], mat[r-1-j][j] = mat[r-1-j][j], mat[i][j]

d
ef print_mat(mat, r, c):
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = ' ')
        print('\n')

if __name__ == "__main__":
    mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print_mat(mat,len(mat),len(mat[0]))
    anticlock_ninety(mat,len(mat),len(mat[0]))
    print_mat(mat,len(mat),len(mat[0]))