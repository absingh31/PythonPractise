class Solution:

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        num_letter_map = {
                '1': '',
                '2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz',
                '0': ''
                }
        result = ['']
        for i in digits:
            if num_letter_map[i] == '': continue

            newresult = []
            for j in num_letter_map[i]:
                newresult += [e + j for e in result]
            result = newresult

        return result


if __name__ == '__main__':
    print Solution().letterCombinations('234')
