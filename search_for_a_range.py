class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if len(A) == 0: return [-1, -1]
        return [self._bsl(A, target), self._bsr(A, target)]


    def _bsl(self, ary, t):
        l = 0
        r = len(ary) - 1

        lastidx = r

        while l <= r:
            m = (l + r) / 2
            if ary[m] == t:
                if m < lastidx:
                    lastidx = m
                r = m - 1
            elif ary[m] < t:
                l = m + 1
            else:
                r = m - 1

        if ary[lastidx] == t:
            return lastidx
        else:
            return - 1

    def _bsr(self, ary, t):
        l = 0
        r = len(ary) - 1

        lastidx = l

        while l <= r:
            m = (l + r) / 2
            if ary[m] == t:
                if m > lastidx:
                    lastidx = m
                l = m + 1
            elif ary[m] < t:
                l = m + 1
            else:
                r = m - 1

        if ary[lastidx] == t:
            return lastidx
        else:
            return - 1

if __name__ == '__main__':
    print Solution().searchRange([5, 7, 7, 8, 8, 8, 10], 8)
