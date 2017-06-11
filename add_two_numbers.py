# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        newroot = ListNode(0)

        newroot.val = (l1.val + l2.val) % 10
        add = (l1.val + l2.val) / 10

        node = newroot

        while True:
            l1 = l1.next
            l2 = l2.next
            if l1 is None or l2 is None:
                break

            v = (add + l1.val + l2.val) % 10
            add = (add + l1.val + l2.val) / 10

            newnode = ListNode(v)
            node.next = newnode
            node = newnode

        if l1 is not None:
            while l1 is not None:
                v = (add + l1.val) % 10
                add = (add + l1.val) / 10
                newnode = ListNode(v)
                node.next = newnode
                node = newnode

                l1 = l1.next

        if l2 is not None:
            while l2 is not None:
                v = (add + l2.val) % 10
                add = (add + l2.val) / 10
                newnode = ListNode(v)
                node.next = newnode
                node = newnode

                l2 = l2.next

        if add != 0:
            newnode = ListNode(add)
            node.next = newnode

        return newroot
