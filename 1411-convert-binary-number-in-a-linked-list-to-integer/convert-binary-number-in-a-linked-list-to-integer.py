class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        result = 0
        curr = head

        while curr:
            result = result * 2 + curr.val
            curr = curr.next

        return result