class Solution:
    # @return a boolean
    def isValid(self, s):
        pair = {')': '(', ']': '[', '}': '{'}
        leftset = set(list('({['))
        rightset = set(list(']})'))

        if len(s) % 2 != 0:
            return False
        if len(s) == 0:
            return True

        if s[0] in rightset:
            return False

        stack = [s[0]]

        for i in range(1, len(s)):
            if s[i] in leftset:
                stack.append(s[i])
            elif s[i] in rightset:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if left != pair[s[i]]:
                    return False

        if len(stack) > 0:
            return False
        else:
            return True

if __name__ == '__main__':
    print Solution().isValid('[[[]]]')
    print Solution().isValid('[](){}')
    print Solution().isValid('[]){}')

