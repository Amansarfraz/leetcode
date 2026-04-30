class Solution(object):
    def numComponents(self, head, nums):
        nums_set = set(nums)
        count = 0
        
        curr = head
        
        while curr:
            # start/end of a component
            if curr.val in nums_set and (not curr.next or curr.next.val not in nums_set):
                count += 1
            
            curr = curr.next
        
        return count