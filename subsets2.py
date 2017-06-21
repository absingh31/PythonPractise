class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        total_result = []
        for i in range(0, len(S) + 1):
            result = set()
            self.iter(S, 0, i, [], result)
            total_result += sorted(list(result))

        return [list(x) for x in total_result]

    def iter(self, S, start, level, result, allresult):
        if level == 0:
            allresult.add(tuple(sorted(result)))
        for i in range(start, len(S)):
            self.iter(S, i + 1, level - 1, result + [S[i]], allresult)

if __name__ == '__main__':
    print Solution().subsets([1, 2, 2])
