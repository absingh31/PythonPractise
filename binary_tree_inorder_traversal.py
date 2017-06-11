# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []

        s = []

        while root or len(s) > 0:
            while root:
                s.append(root)
                root = root.left
            if len(s) > 0:
                root = s.pop()
                result.append(root.val)
                root = root.right


        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print Solution().inorderTraversal(root)
