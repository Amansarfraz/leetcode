class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            total = 0
            needed_days = 1
            
            for w in weights:
                if total + w > mid:
                    needed_days += 1
                    total = 0
                
                total += w
            
            if needed_days <= days:
                right = mid
            else:
                left = mid + 1
        
        return left