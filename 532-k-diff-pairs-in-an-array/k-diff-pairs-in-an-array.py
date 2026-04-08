from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0  # absolute difference cannot be negative
        
        count = Counter(nums)
        result = 0
        
        if k == 0:
            # Count numbers with frequency >= 2
            for val in count.values():
                if val >= 2:
                    result += 1
        else:
            # Count unique pairs with difference k
            for num in count:
                if num + k in count:
                    result += 1
        
        return result