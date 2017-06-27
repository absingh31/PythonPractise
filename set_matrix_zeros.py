class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        if n == 0: return

        flagary = [0] * (m + n)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    flagary[i] = 1
                    flagary[j + m] = 1

        for i in range(m + n):
            if flagary[i] == 0:
                continue
            if i < m:
                for j in range(n):
                    matrix[i][j] = 0
            else:
                for j in range(m):
                    matrix[j][i - m] = 0

if __name__ == '__main__':
    import pprint
    m = [[1, 0, 0, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
    pprint.pprint(m)
    Solution().setZeroes(m)
    pprint.pprint(m)

