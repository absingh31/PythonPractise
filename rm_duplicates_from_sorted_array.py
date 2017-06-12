class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0: return 0

        i = 0

        for j in range(1, n):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]

        return i + 1

if __name__ == '__main__':
    print Solution().removeDuplicates([1, 1])
