class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        result = [num[:]]
        perm = self.next_permutation(num)
        while perm != None:
            result.append(perm[:])
            perm = self.next_permutation(perm)
        return result

    def next_permutation(self, num):
        n = len(num)

        fstdesc = None
        chgpst = None
        for i in range(n - 2, -1, -1):
            if num[i] < num[i + 1]:
                fstdesc = i
                break

        if fstdesc == None:
            return None

        for i in range(n - 1, -1, -1):
            if num[i] > num[fstdesc]:
                chgpst = i
                break

        num[fstdesc], num[chgpst] = num[chgpst], num[fstdesc]

        i = fstdesc + 1
        j = n - 1

        while i < j:
            num[i], num[j] = num[j], num[i]
            i += 1
            j -= 1

        return num


if __name__ == '__main__':
    print Solution().permuteUnique([1, 1, 1])
