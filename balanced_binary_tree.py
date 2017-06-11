# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.balancedheight(root) >= 0

    def abs(self, v):
        if v > 0:
            return v
        else:
            return -v

    def balancedheight(self, root):
        if root is None: return 0

        left = self.balancedheight(root.left)
        right = self.balancedheight(root.right)

        if left < 0 or right < 0 or self.abs(left - right) > 1:
            return -1

        return max(left, right) + 1
