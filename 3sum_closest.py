class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        def abs(x):
            if x > 0: return x
            else: return -x

        n = len(num)

        num.sort()

        min_gap = 999999
        result = 999999

        for i in xrange(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                gap = abs(target - sum)

                if gap < min_gap:
                    min_gap = gap
                    result = sum

                if sum < target:
                    j += 1
                else:
                    k -= 1

        return result

if __name__ == '__main__':
    print Solution().threeSumClosest([-1, 2, 1, -4], 1)
