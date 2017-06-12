#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        height.append(0)
        n = len(height)

        stack = []
        i = 0
        maxarea = 0

        while i < n:
            if len(stack) == 0 or height[stack[-1]] <= height[i]:
                stack.append(i)
            else:
                while len(stack) > 0 and height[stack[-1]] > height[i]:
                    j = stack.pop()
                    if len(stack):
                        maxarea = max(maxarea, (i - stack[-1] - 1) * height[j])
                    else:
                        maxarea = max(maxarea, i * height[j])
                stack.append(i)
            i += 1

        return maxarea

if __name__ == '__main__':
    print Solution().largestRectangleArea([2, 1, 2])
