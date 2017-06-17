# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        sorted_intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        i = 0
        while i < len(sorted_intervals) - 1:
            if sorted_intervals[i].end >= sorted_intervals[i+1].start:
                sorted_intervals[i].end = max(sorted_intervals[i+1].end, \
                                              sorted_intervals[i].end)
                del sorted_intervals[i+1]
            else:
                i += 1

        return sorted_intervals



if __name__ == '__main__':
    input = [Interval(2, 6), Interval(1, 3), Interval(8, 10), Interval(15, 18)]
    result = Solution().merge(input)
    for i in result:
        print '(%d, %d)' % (i.start, i.end)
