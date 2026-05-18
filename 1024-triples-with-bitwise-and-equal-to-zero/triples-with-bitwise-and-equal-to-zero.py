from collections import defaultdict

class Solution(object):
    def countTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = defaultdict(int)
        
        # Store all pair AND results
        for a in nums:
            for b in nums:
                count[a & b] += 1
        
        result = 0
        
        # Check triples
        for c in nums:
            for val in count:
                if (val & c) == 0:
                    result += count[val]
        
        return result