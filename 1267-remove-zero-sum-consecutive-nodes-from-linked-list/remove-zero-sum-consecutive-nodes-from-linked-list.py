# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prefix = 0
        seen = {}
        node = dummy

        while node:
            prefix += node.val
            seen[prefix] = node
            node = node.next

        prefix = 0
        node = dummy

        while node:
            prefix += node.val
            node.next = seen[prefix].next
            node = node.next

        return dummy.next