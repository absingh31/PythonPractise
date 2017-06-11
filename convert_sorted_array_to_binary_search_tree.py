# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.build(num)

    def build(self, num):
        if len(num) == 0: return None
        if len(num) == 1: return TreeNode(num[0])

        mid = len(num) / 2

        leftary = num[:mid]
        rightary = num[mid+1:]

        node = TreeNode(num[mid])

        node.left = self.build(leftary)
        node.right = self.build(rightary)

        return node
