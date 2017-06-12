# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        if n == 0: return [None]
        else: return self.generate(1, n)

    def generate(self, s, e):
        if s > e: return [None]
        subtrees = []
        for i in range(s, e + 1):
            lefttrees = self.generate(s, i - 1)
            righttrees = self.generate(i + 1, e)

            for lefttree in lefttrees:
                for righttree in righttrees:
                    node = TreeNode(i)
                    node.left = lefttree
                    node.right = righttree

                    subtrees.append(node)

        return subtrees
