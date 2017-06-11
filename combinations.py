class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result = set()
        self.iter(range(1, n + 1), 0, k, [], result)
        return map(list, result)

    def iter(self, s, start, level, current_val, result):
        if level == 0:
            result.add(tuple(sorted(current_val)))
            return

        n = len(s)

        for i in range(start, n):
            self.iter(s, i + 1, level - 1, current_val + [s[i]], result)


if __name__ == '__main__':
    print Solution().combine(4, 2)


