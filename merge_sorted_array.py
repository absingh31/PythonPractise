class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        idx_a = m - 1
        idx_b = n - 1
        i = m + n - 1

        while idx_a >= 0 and idx_b >= 0:
            if A[idx_a] > B[idx_b]:
                A[i] = A[idx_a]
                idx_a -= 1
            else:
                A[i] = B[idx_b]
                idx_b -= 1
            i -= 1

        while idx_a >= 0:
            A[i] = A[idx_a]
            i -= 1
            idx_a -= 1

        while idx_b >= 0:
            A[i] = B[idx_b]
            i -= 1
            idx_b -= 1
