from sortedcontainers import SortedDict

class Solution(object):
    def oddEvenJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        n = len(arr)
        
        odd = [False] * n
        even = [False] * n
        
        odd[-1] = even[-1] = True
        
        sd = SortedDict()
        sd[arr[-1]] = n - 1
        
        for i in range(n - 2, -1, -1):
            
            # Odd jump -> next greater or equal
            idx = sd.bisect_left(arr[i])
            
            if idx < len(sd):
                odd[i] = even[sd.peekitem(idx)[1]]
            
            # Even jump -> next smaller or equal
            idx = sd.bisect_right(arr[i]) - 1
            
            if idx >= 0:
                even[i] = odd[sd.peekitem(idx)[1]]
            
            sd[arr[i]] = i
        
        return sum(odd)