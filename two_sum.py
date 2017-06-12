class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        idxmap = {}
        for i, v in enumerate(num):
            if v not in idxmap:
                idxmap[v] = []
            idxmap[v].append(i)

        for i, v in enumerate(num):
            u = target - v
            if u not in idxmap:
                continue
            else:
                if u == v and len(idxmap[u]) == 2:
                    return (min(idxmap[u]) + 1, \
                            max(idxmap[u]) + 1)
                if u != v:
                    return (min(idxmap[u][0], idxmap[v][0]) + 1, \
                            max(idxmap[u][0], idxmap[v][0]) + 1)

if __name__ == '__main__':
    print Solution().twoSum([2, 7, 11, 13], 9)

