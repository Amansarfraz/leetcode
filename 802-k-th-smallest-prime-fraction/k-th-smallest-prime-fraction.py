import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        heap = []
        
        # push smallest fraction for each numerator
        for i in range(n - 1):
            heapq.heappush(heap, (arr[i] / float(arr[n - 1]), i, n - 1))
        
        # extract k-1 times
        for _ in range(k - 1):
            val, i, j = heapq.heappop(heap)
            
            if j - 1 > i:
                heapq.heappush(heap, (arr[i] / float(arr[j - 1]), i, j - 1))
        
        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]