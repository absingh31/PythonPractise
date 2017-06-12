class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)

        if n == 1:
            return True

        furthest_position = A[0]

        if furthest_position >= n - 1:
            return True

        if furthest_position == 0:
            return False

        for i in range(1, n):
            if furthest_position >= i and A[i] + i >= n - 1:
                return True
            if furthest_position <= i and A[i] == 0:
                return False
            furthest_position = max(furthest_position,  A[i] + i)

        return False

if __name__ == '__main__':
    print Solution().canJump([2, 3, 1, 1, 4])
    print Solution().canJump([3, 2, 1, 0, 4])
    print Solution().canJump(range(25000, 0, -1) + [1, 0, 0])
