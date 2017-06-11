# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self._build(inorder, postorder)

    def _build(self, inorder, postorder):
        if len(inorder) == 0:
            return None

        rootvalue = postorder.pop()
        idx = inorder.index(rootvalue)

        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]

        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):]

        node = TreeNode(rootvalue)
        node.left = self._build(inorder_left, postorder_left)
        node.right = self._build(inorder_right, postorder_right)

        return node
