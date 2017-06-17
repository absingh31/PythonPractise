class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):

        validflag = [False] * len(s)

        stack = []

        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    continue
                else:
                    left = stack.pop()
                    validflag[left] = True
                    validflag[i] = True

        maxlen = 0
        curlen = 0
        for i in range(len(validflag)):
            if validflag[i]:
                curlen += 1
            else:
                maxlen = max(maxlen, curlen)
                curlen = 0

        maxlen = max(maxlen, curlen)
        return maxlen

if __name__ == '__main__':
    print Solution().longestValidParentheses(')()())')
    print Solution().longestValidParentheses('()')
