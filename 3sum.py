class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        if len(num) < 3: return []
        num.sort()

        val = 0
        result = []

        n = len(num)

        for i in xrange(n - 2):
            if i >= 1 and num[i] == num[i - 1]:
                continue
            j = i + 1
            k = n - 1
            left = val - num[i]
            while j < k:
                if num[j] + num[k] == left:
                    result.append([num[i], num[j], num[k]])
                    while j < k:
                        j += 1
                        k -= 1
                        if num[j] != num[j - 1] or num[k] != num[k + 1]:
                            break
                elif num[j] + num[k] < left:
                    while j < k:
                        j += 1
                        if num[j] != num[j - 1]:
                            break
                else:
                    while j < k:
                        k -= 1
                        if num[k] != num[k + 1]:
                            break
        return result

if __name__ == '__main__':
    print Solution().threeSum([-2, 0, 1, 1, 2])
