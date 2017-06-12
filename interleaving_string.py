class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l1 + l2 != l3: return False

        result = [[False] * (l2 + 1) for i in range(l1 + 1)]

        result[0][0] = True

        for i in range(1, l1 + 1):
            if result[i - 1][0] and s1[i - 1] == s3[i - 1]:
                result[i][0] = True

        for i in range(1, l2 + 1):
            if result[0][i - 1] and s2[i - 1] == s3[i - 1]:
                result[0][i] = True

        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                result[i][j] = result[i - 1][j] and s3[i + j - 1] == s1[i - 1] or \
                               result[i][j - 1] and s3[i + j - 1] == s2[j - 1]

        return result[l1][l2]


if __name__ == '__main__':
    print Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    print Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc')



