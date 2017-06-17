class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0: return 0

        j = 0
        for i in range(1, n):
            if A[i] != A[j]:
                j += 1
                A[j] = A[i]

        return j + 1
