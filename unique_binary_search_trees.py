class Solution:
    # @return an integer
    def numTrees(self, n):
        result = [0] * (n + 1)

        result[0] = 1
        result[1] = 1

        for i in range(2 , n + 1):
            for k in range(1, i + 1):
                result[i] += result[k - 1] * result[i - k]

        return result[-1]

if __name__ == '__main__':
    print Solution().numTrees(4)
