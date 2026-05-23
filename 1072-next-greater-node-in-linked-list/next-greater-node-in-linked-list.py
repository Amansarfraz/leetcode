# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        
        # Convert linked list to array
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        n = len(nums)
        result = [0] * n
        
        # Stack stores indices
        stack = []
        
        for i in range(n):
            
            # Find next greater element
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                result[index] = nums[i]
            
            stack.append(i)
        
        return result