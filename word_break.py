class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if len(dict) == 0: return False
        if len(s) == 0: return True

        minlen = min([len(w) for w in dict])
        if len(s) < minlen:
            return False

        alpha = set(list(s))
        alphaindict = set.union(*[set(list(w)) for w in dict])
        if len(alpha - alphaindict) > 0:
            return False

        return self._wordBreak(s, dict)

    def _wordBreak(self, s, dict):
        if len(s) == 0: return True

        for word in dict:
            if s.startswith(word):
                sub_s = s[len(word):]
                if self.wordBreak(sub_s, dict):
                    return True

        return False


if __name__ == '__main__':
    print Solution().wordBreak('leetcode2', ['leet', 'code'])
