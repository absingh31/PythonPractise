# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None: return

        self.flatten(root.left)
        self.flatten(root.right)

        p = root.left

        if p is None: return

        while p.right:
            p = p.right

        p.right = root.right
        root.right = root.left
        root.left = None


