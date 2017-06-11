# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self._build(preorder, inorder)

    def _build(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        rootvalue = preorder.pop(0)

        nodeidx = inorder.index(rootvalue)
        inorder_left = inorder[:nodeidx]
        inorder_right = inorder[nodeidx+1:]

        preorder_left = preorder[:len(inorder_left)]
        preorder_right = preorder[len(inorder_left):]

        node = TreeNode(rootvalue)

        node.left = self._build(preorder_left, inorder_left)
        node.right = self._build(preorder_right, inorder_right)

        return node

if __name__ == '__main__':
    node = Solution().buildTree([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 6, 3])
    print node.left.val
    print node.val
    print node.right.val
