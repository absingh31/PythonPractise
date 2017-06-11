# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        if root == None: return []

        travel = []
        visit = []
        result = []

        travel.append(root)

        while len(travel) > 0:
            node = travel.pop()

            visit.append(node)
            if node.left:
                travel.append(node.left)
            if node.right:
                travel.append(node.right)

        while len(visit) > 0:
            node = visit.pop()
            result.append(node.val)

        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print Solution().postorderTraversal(root)
