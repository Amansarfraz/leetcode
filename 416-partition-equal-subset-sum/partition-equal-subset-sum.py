class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        
        # If total is odd → impossible
        if total % 2 != 0:
            return False
        
        target = total // 2
        possible = set([0])
        
        for num in nums:
            new = set()
            for s in possible:
                if s + num == target:
                    return True
                new.add(s + num)
            possible |= new
        
        return target in possible