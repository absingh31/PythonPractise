# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.nodes = []

        self._trav(root, lambda x: self.nodes.append(x))

        wrong1 = None
        wrong2 = None

        for i in range(0, len(self.nodes) - 1):
            if self.nodes[i].val > self.nodes[i + 1].val:
                wrong1 = self.nodes[i]
                break

        for i in range(len(self.nodes) - 1, 0, -1):
            if self.nodes[i].val < self.nodes[i - 1].val:
                wrong2 = self.nodes[i]
                break

        wrong1.val, wrong2.val = wrong2.val, wrong1.val

        return root


    def _trav(self, root, handler):
        if not root: return

        self._trav(root.left, handler)
        handler(root)
        self._trav(root.right, handler)

