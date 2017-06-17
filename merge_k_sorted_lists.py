# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        return self.merge_helper(lists, 0, len(lists) - 1)

    def merge_helper(self, lists, l, r):
        if l < r:
            m = (l + r) / 2
            return self.merge_two_lists(self.merge_helper(lists, l, m), self.merge_helper(lists, m + 1, r))
        return lists[l]

    def merge_two_lists(self, l1, l2):
        p = dummy = ListNode(-1)

        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1:
            p.next = l1
        else:
            p.next = l2

        return dummy.next

if __name__ == '__main__':
    print Solution().mergeKLists([ListNode(1), ListNode(0)])
