class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = []
        inword = False
        inspace = True

        cur = ''
        for i in range(len(s)):
            if s[i] != ' ':
                if inspace:
                    cur = s[i]
                else:
                    cur += s[i]
                inword = True
                inspace = False
            else:
                if inword:
                    words.append(cur)
                    inword = False
                    cur = ''
                    inspace = True

        if len(cur) > 0:
            words.append(cur)

        words.reverse()
        return ' '.join(words)

if __name__ == '__main__':
    print Solution().reverseWords(' 1')
