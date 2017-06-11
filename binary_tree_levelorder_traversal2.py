# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None: return []
        q = [root]

        result = []

        while len(q) > 0:
            tmpq = []
            cur_level_node = []
            while len(q) > 0:
                node = q.pop(0)
                cur_level_node.append(node.val)
                if node.left:
                    tmpq.append(node.left)
                if node.right:
                    tmpq.append(node.right)

            q = tmpq
            result.append(cur_level_node)

        result.reverse()
        return result

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print Solution().levelOrderBottom(root)
