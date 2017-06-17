class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'

        def _add(ary1, ary2):
            ary1 = ary1[::-1]
            ary2 = ary2[::-1]

            l1 = len(ary1)
            l2 = len(ary2)

            result = []

            i = 0
            extra = 0

            while i < min(l1, l2):
                v = (ary1[i] + ary2[i] + extra) % 10
                extra = (ary1[i] + ary2[i] + extra) / 10
                result.append(v)
                i += 1

            if i == l1:
                while i < l2:
                    v = (ary2[i] + extra) % 10
                    extra = (ary2[i] + extra) / 10
                    result.append(v)
                    i += 1
            elif i == l2:
                while i < l1:
                    v = (ary1[i] + extra) % 10
                    extra = (ary1[i] + extra) / 10
                    result.append(v)
                    i += 1

            if extra != 0:
                result.append(extra)

            return result[::-1]


        zero = ord('0')
        ary1 = [ord(c) - zero for c in num1]
        ary2 = [ord(c) - zero for c in num2]

        result = None

        for i in range(len(ary2) - 1, -1, -1):
            cur_val = ary2[i]
            cur_result = [0] * (len(ary2) - i - 1)
            extra = 0

            for j in range(len(ary1) - 1, -1, -1):
                cur_result.append((cur_val * ary1[j] + extra) % 10)
                extra = ((cur_val * ary1[j]) + extra) / 10

            if extra != 0:
                cur_result.append(extra)

            if result is None:
                result = cur_result[::-1]
            else:
                result = _add(result, cur_result[::-1])

        return ''.join(map(str, result))

if __name__ == '__main__':
    print Solution().multiply('123', '11')
