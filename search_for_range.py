class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return [self._search_left(A, target), self._search_right(A, target)]

    def _search_left(self, A, target):
        l = 0
        r = len(A) - 1

        last_position = -1
        find = False

        while l <= r:
            mid = (l + r) / 2
            if A[mid] == target:
                find = True
                r = mid - 1
            elif A[mid] < target:
                last_position = mid
                l = mid + 1
            else:
                r = mid - 1

        if find:
            return last_position + 1
        else:
            return -1


    def _search_right(self, A, target):
        l = 0
        r = len(A) - 1

        last_position = len(A)
        find = False

        while l <= r:
            mid = (l + r) / 2
            if A[mid] == target:
                find = True
                l = mid + 1
            elif A[mid] < target:
                l = mid + 1
            else:
                last_position = mid
                r = mid - 1

        if find:
            return last_position - 1
        else:
            return -1

if __name__ == '__main__':
    print Solution().searchRange([5, 7, 7, 8, 8], 5)
