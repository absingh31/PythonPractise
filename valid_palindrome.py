class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        s = s.lower()
        charlist = []
        for c in s:
            if 'a' <= c <= 'z' or '0' <= c <= '9':
                charlist.append(c)
        newstring = ''.join(charlist)
        return newstring == newstring[::-1]

if __name__ == '__main__':
    print Solution().isPalindrome('A man, a plan, a canal: Panama')
