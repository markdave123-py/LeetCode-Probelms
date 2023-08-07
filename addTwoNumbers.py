# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = ListNode()
        curr = head
        carry = 0

        while (l1 != None or l2 != None or carry != 0):
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            curr.next = ListNode(total % 10)
            carry = total // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next


        return head.next