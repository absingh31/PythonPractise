# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.isvalid(root, -100000, 100000)

    def isvalid(self, root, lower, upper):
        if root == None: return True

        return root.val > lower and root.val < upper and \
                self.isvalid(root.left, lower, root.val) and \
                self.isvalid(root.right, root.val, upper)
