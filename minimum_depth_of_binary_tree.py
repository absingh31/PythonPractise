# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        return self._min_depth(root)

    def _min_depth(self, root):
        if root is None: return 0

        if root.left is None and root.right is None: return 1

        if root.left and root.right is None:
            return self._min_depth(root.left) + 1
        elif root.right and root.left is None:
            return self._min_depth(root.right) + 1

        return min(self._min_depth(root.left), self._min_depth(root.right)) + 1

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print Solution().minDepth(root)
