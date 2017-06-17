class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0: return ''

        prefix = ''

        minlen = min(map(lambda x: len(x), strs))
        if minlen == 0: return ''

        for i in range(minlen):
            c = strs[0][i]
            finished = True
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    finished = False
                    break

            if finished:
                prefix += c
            else:
                return prefix

        return prefix

if __name__ == '__main__':
    print Solution().longestCommonPrefix(['aca', 'cba'])
