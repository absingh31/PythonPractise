class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if len(A) == 0: return False
        if len(A) == 1:
            if target == A[0]:
                return True
            else:
                return False

        p = 0
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                p = i
                break

        lidx = self.bs(A, 0, p - 1, target)
        ridx = self.bs(A, p, len(A) - 1, target)

        return not (lidx == ridx == -1)

    def bs(self, A, l, r, t):
        if l > r: return -1

        while l <= r:
            m = (l + r) / 2
            if A[m] == t:
                return m
            elif A[m] < t:
                l = m + 1
            else:
                r = m - 1

        return -1

if __name__ == '__main__':
    print Solution().search([1, 2, 3, 4, 5, 5, 4, 3, 2, 1], 6)
