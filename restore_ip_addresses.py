class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.result = set()
        self._split([], s, 4)
        return list(self.result)

    def _split(self, heads, s, n):
        if len(s) == 0 or n == 0:
            return False

        if n == 1:
            if int(s) > 255 or (s.startswith('0') and s != '0'):
                return False
            else:
                self.result.add('.'.join(heads) + '.' + s)
                return True
        else:
            for i in range(3):
                head = s[:i+1]
                if int(head) > 255 or (head.startswith('0') and head != '0'):
                    return False
                else:
                    heads.append(head)
                    result = self._split(heads, s[i+1:], n - 1)
                    heads.pop()

if __name__ == '__main__':
    print Solution().restoreIpAddresses('25525511135')
    print Solution().restoreIpAddresses('0000')
    print Solution().restoreIpAddresses('010010')
