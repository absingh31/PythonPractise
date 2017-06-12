# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        return self._max_depth(root)

    def _max_depth(self, root):
        if root is None: return 0
        else:
            return max(self._max_depth(root.left), self._max_depth(root.right)) + 1

