class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)

        if m == 0 and n != 0:
            if n % 2 == 0:
                return B[(n - 1) / 2] / 2.0 + B[n / 2] / 2.0
            else:
                return B[n / 2]
        if n == 0 and m != 0:
            if m % 2 == 0:
                return A[(m - 1) / 2] / 2.0 + A[m / 2] / 2.0
            else:
                return A[m / 2]

        if (m + n) % 2 == 0:
            return (self.kth(A, 0, m - 1, B, 0, n - 1, (m + n) / 2)) / 2.0 + \
                   (self.kth(A, 0, m - 1, B, 0, n - 1, (m + n) / 2 + 1)) / 2.0
        else:
            return self.kth(A, 0, m - 1, B, 0, n - 1, (m + n) / 2 + 1)

    def kth(self, A, al, ar, B, bl, br, k):
        m = ar - al + 1
        n = br - bl + 1

        if m > n:
            return self.kth(B, bl, br, A, al, ar, k)
        if m == 0:
            return B[bl + k - 1]
        if k == 1:
            return min(A[al], B[bl])

        ia = min(m, k / 2)
        ib = k - ia

        if A[al + ia - 1] < B[bl + ib - 1]:
            return self.kth(A, al + ia, ar, B, bl, br, k - ia)
        elif A[al + ia - 1] > B[bl + ib - 1]:
            return self.kth(A, al, ar, B, bl + ib, br, k - ib)
        else:
            return A[al + ia - 1]

if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1, 2], [1, 2])
