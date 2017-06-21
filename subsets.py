class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        total_result = []
        for i in range(0, len(S) + 1):
            result = []
            self.iter(S, 0, i, [], result)
            total_result += sorted(result)

        return total_result

    def iter(self, S, start, level, result, allresult):
        if level == 0:
            allresult.append(sorted(result))
        for i in range(start, len(S)):
            self.iter(S, i + 1, level - 1, result + [S[i]], allresult)

if __name__ == '__main__':
    print Solution().subsets([4, 1, 0])
