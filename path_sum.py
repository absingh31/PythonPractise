# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root is None: return False
        return self.find(root, 0, sum)

    def find(self, root, cur_val, target):
        if root is None and cur_val != target: return False
        if root is None and cur_val == target: return True

        if root.left and root.right is None:
            return self.find(root.left, cur_val + root.val, target)
        if root.right and root.left is None:
            return self.find(root.right, cur_val + root.val, target)

        lresult = self.find(root.left, cur_val + root.val, target)
        rresult = self.find(root.right, cur_val + root.val, target)

        return lresult or rresult


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.left.left = TreeNode(5)

    print Solution().hasPathSum(root, 15)
