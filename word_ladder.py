#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if start == end: return 0

        alpha = list('abcdefghijklmnopqrstuvwxyz')

        dict.add(end)
        dict.add(start)

        q = [start]
        visited = set([start])
        distmap = {start: 0}

        while len(q):
            u = q.pop(0)

            charlist = list(u)
            n = len(charlist)
            for i in range(n):
                old = charlist[i]
                for c in alpha:
                    if c == old: continue
                    charlist[i] = c
                    newword = ''.join(charlist)
                    if newword in dict and not newword in visited:
                        distmap[newword] = distmap[u] + 1
                        visited.add(newword)
                        q.append(newword)

                        if newword == end:
                            return distmap[end] + 1
                charlist[i] = old

        return distmap.get(end, -1) + 1


if __name__ == '__main__':
    print Solution().ladderLength('hit', 'cog', set(['hot', 'dot', 'dog', 'lot', 'log']))
    print Solution().ladderLength('a', 'c', set(['a', 'b', 'c']))
