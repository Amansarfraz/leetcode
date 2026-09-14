from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Count the frequency of each number
        count = Counter(nums)
        
        # Sort using a custom key:
        # 1. count[x] (ascending order of frequency)
        # 2. -x (descending order of the value itself when frequencies match)
        return sorted(nums, key=lambda x: (count[x], -x))
