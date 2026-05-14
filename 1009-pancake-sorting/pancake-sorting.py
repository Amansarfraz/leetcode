class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        res = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            max_idx = arr.index(max(arr[:size]))
            
            if max_idx == size - 1:
                continue
            
            # Flip max element to front
            if max_idx != 0:
                arr[:max_idx + 1] = reversed(arr[:max_idx + 1])
                res.append(max_idx + 1)
            
            # Flip max element to correct position
            arr[:size] = reversed(arr[:size])
            res.append(size)
        
        return res