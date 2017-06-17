class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        visited = {}
        for v in num:
            visited[v] = False

        longest = 0

        for v in visited:
            if visited[v]: continue
            else:
                length = 1
                tmp = v
                while tmp - 1 in visited:
                    visited[tmp - 1] = True
                    length += 1
                    tmp -= 1
                tmp = v
                while tmp + 1 in visited:
                    visited[tmp + 1] = True
                    length += 1
                    tmp += 1
                longest = max(longest, length)

        return longest

if __name__ == '__main__':
    print Solution().longestConsecutive([100, 4, 200, 3, 2, 1])
