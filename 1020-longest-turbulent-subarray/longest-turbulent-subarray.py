class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        
        if n == 1:
            return 1
        
        left = 0
        result = 1
        
        for right in range(1, n):
            
            cmp = 0
            if arr[right - 1] < arr[right]:
                cmp = 1
            elif arr[right - 1] > arr[right]:
                cmp = -1
            
            if cmp == 0:
                left = right
            
            elif right == n - 1 or \
                cmp * (
                    1 if arr[right] < arr[right + 1]
                    else -1 if arr[right] > arr[right + 1]
                    else 0
                ) != -1:
                
                result = max(result, right - left + 1)
                left = right
        
        return result