# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.max = -99999999

        self.dfs(root)

        return self.max

    def dfs(self, root):
        if root is None: return 0

        lval = self.dfs(root.left)
        rval = self.dfs(root.right)

        sum = root.val

        if lval > 0: sum += lval
        if rval > 0: sum += rval

        self.max = max(self.max, sum)

        if max(lval, rval) > 0:
            return max(lval, rval) + root.val
        else:
            return root.val
