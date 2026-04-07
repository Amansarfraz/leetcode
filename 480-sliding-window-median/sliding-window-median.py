from sortedcontainers import SortedList

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = SortedList()
        result = []
        
        for i in range(len(nums)):
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k])
            
            if i >= k - 1:
                if k % 2 == 0:
                    median = (window[k//2 - 1] + window[k//2]) / 2.0
                else:
                    median = float(window[k//2])
                result.append(median)
        
        return result