class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        """
        loop the bounds of the graph and mark all O can be travelled
        as +
        and at last set all left O as X and set + as O
        """
        if len(board) == 0: return board

        m = len(board)
        n = len(board[0])

        def handler(board, i, j):
            board[i][j] = '+'

        for i in range(m):
            if board[i][0] == 'O':
                self._dp(board, i, 0, handler)

        for i in range(m):
            if board[i][n - 1] == 'O':
                self._dp(board, i, n - 1, handler)

        for i in range(n):
            if board[0][i] == 'O':
                self._dp(board, 0, i, handler)

        for i in range(n):
            if board[m - 1][i] == 'O':
                self._dp(board, m - 1, i, handler)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '+':
                    board[i][j] = 'O'

        return board

    def _dp(self, board, i, j, handler):
        """
        Use recursive will cause runtime error
        """
        m = len(board)
        n = len(board[0])

        st = [(i, j)]

        while len(st) > 0:
            a, b = st.pop()
            handler(board, a, b)
            for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if self._inbound(a + x, b + y, m, n) and board[a + x][b + y] == 'O':
                    st.append((a + x, b + y))

    def _inbound(self, i, j, m, n):
        if 0 <= i < m and 0 <= j < n:
            return True
        else:
            return False

if __name__ == '__main__':
    board = [
            "XXXX",
            "XOOX",
            "XXOX",
            "XOXX"
            ]
    board = [list(x) for x in board]

    print Solution().solve(board)


