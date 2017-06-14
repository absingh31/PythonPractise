# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        if root is None: return []
        total_result = []
        self.find(root, [], sum, total_result)
        return  total_result

    def find(self, root, cur_vector, target, total_result):
        if root is None and sum(cur_vector) == target:
            total_result.append(cur_vector)
            return
        if root is None and sum(cur_vector) != target:
            return

        if root.right is None:
            self.find(root.left, cur_vector[:] + [root.val], target, total_result)
            return

        if root.left is None and root.right:
            self.find(root.right, cur_vector[:] + [root.val], target, total_result)
            return

        self.find(root.left, cur_vector[:] + [root.val], target, total_result)
        self.find(root.right, cur_vector[:] + [root.val], target, total_result)

