class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):

        for i in range(9):
            ary = [False] * 9
            for j in range(9):
                if not self.isvalid(board[i][j], ary):
                    return False

        for i in range(9):
            ary = [False] * 9
            for j in range(9):
                if not self.isvalid(board[j][i], ary):
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                ary = [False] * 9
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if not self.isvalid(board[k][l], ary):
                            return False

        return True

    def isvalid(self, cur_val, cur_array):
        if cur_val == '.':
            return True
        cur_val = int(cur_val)
        if cur_val < 1 or cur_val > 9:
            return False
        if cur_array[cur_val - 1] == True:
            return False
        else:
            cur_array[cur_val - 1] = True
            return True

if __name__ == '__main__':
    print Solution().isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
