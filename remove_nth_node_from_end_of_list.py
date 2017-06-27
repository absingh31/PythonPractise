# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if not head: return head

        tolist = []
        node = head
        while node:
            tolist.append(node)
            node = node.next

        if len(tolist) == 1:
            return None

        # remove last
        if n == 1:
            tolist[-2].next = None
            return head
        elif n == len(tolist):
            head = head.next
            return head
        else:
            tolist[-(n + 1)].next = tolist[-(n - 1)]
            return head

if __name__ == '__main__':
    def print_list(head):
        while head:
            print head.val
            head = head.next
        print

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print_list(head)

    head = Solution().removeNthFromEnd(head, 5)

    print_list(head)
