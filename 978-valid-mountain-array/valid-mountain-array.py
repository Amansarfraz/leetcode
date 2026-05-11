class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        n = len(arr)
        i = 0
        
        # climb up
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1
        
        # peak can't be first or last
        if i == 0 or i == n - 1:
            return False
        
        # go down
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1
        
        return i == n - 1