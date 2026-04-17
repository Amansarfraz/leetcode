# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        # Step 1: count length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        base = n // k
        extra = n % k
        
        res = []
        curr = head
        
        for i in range(k):
            part_head = curr
            size = base + (1 if extra > 0 else 0)
            extra -= 1 if extra > 0 else 0
            
            # move to end of current part
            prev = None
            for j in range(size):
                prev = curr
                if curr:
                    curr = curr.next
            
            # cut the list
            if prev:
                prev.next = None
            
            res.append(part_head)
        
        return res