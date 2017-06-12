class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = 0

        for a in A:
            result ^= a

        return result

if __name__ == '__main__':
    print Solution().singleNumber([1, 2, 2, 1, 3])

