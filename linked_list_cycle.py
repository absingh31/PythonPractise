# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None: return False
        visited = {}
        p = head

        while p and p not in visited:
            visited[p] = True
            p = p.next

        if p is None: return False
        else: return True
