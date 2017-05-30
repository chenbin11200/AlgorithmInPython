# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]


head = ListNode(1)
next = ListNode(2)
head.next = next
next2 = ListNode(3)
next.next = next2

Solution().removeNthFromEnd(head, 2)