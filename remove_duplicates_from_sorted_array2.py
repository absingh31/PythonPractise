class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n == 0: return 0

        j = 0
        cnt = 0
        for i in range(1, n):
            if A[i] != A[j]:
                j += 1
                A[j] = A[i]
                cnt = 0
                continue

            if A[i] == A[j] and cnt == 0:
                j += 1
                A[j] = A[i]
                cnt += 1
                continue

        return j + 1

if __name__ == '__main__':
    A = [1, 1, 2, 3, 3, 3, 4]
    result = Solution().removeDuplicates(A)
    print A[:result]
