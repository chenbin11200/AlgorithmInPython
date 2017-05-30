# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.plus1 = 0

    def copyTheResults(self, node, result):
        while node != None:
            result.next = ListNode(node.val)
            result = result.next
            result.next = None
            if self.plus1 == 1:
                result.val = node.val + 1
                if result.val >= 10:
                    result.val = result.val - 10
                    self.plus1 = 1
                else:
                    self.plus1 = 0
            node = node.next

        if self.plus1 == 1:
            result.next = ListNode(1)
            result = result.next
            result.next = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        resultHead = result = ListNode(0)
        while l1 != None and l2 != None:
            result.next = ListNode(l1.val + l2.val)
            result = result.next
            result.next = None
            if self.plus1 == 1:
                result.val = result.val + 1
                self.plus1 = 0

            if result.val >= 10:
                result.val = result.val - 10
                self.plus1 = 1
            l1 = l1.next
            l2 = l2.next

        if l1 == None:
            self.copyTheResults(l2, result)
        if l2 == None:
            self.copyTheResults(l1, result)

        return resultHead.next