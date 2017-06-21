# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.dfs(root, 0)

    def dfs(self, root, sum):
        if root is None: return 0

        if root.left is None and root.right is None:
            return sum * 10 + root.val

        return self.dfs(root.left, 10 * sum + root.val) + \
                self.dfs(root.right, 10 * sum + root.val)
