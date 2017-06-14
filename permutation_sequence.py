class Solution:
    # @return a string
    def getPermutation(self, n, k):
        s = range(1, n + 1)

        facts = self.factorial(n)

        base = facts[n - 1]
        k -= 1

        result = []
        for i in range(n - 1, -1, -1):
            base = facts[i]
            idx = k / base
            result.append(s[idx])
            k = k % base
            del s[idx]

        return ''.join(map(str, result))

    def factorial(self, n):
        result = [1] * (n + 1)
        for i in range(1, n + 1):
            result[i] *= result[i - 1] * i
        return result


if __name__ == '__main__':
    print Solution().getPermutation(3, 2)
