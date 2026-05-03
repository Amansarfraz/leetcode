import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        workers = []
        
        # (ratio, quality)
        for q, w in zip(quality, wage):
            workers.append((float(w) / q, q))
        
        # sort by ratio
        workers.sort()
        
        max_heap = []
        total_quality = 0
        res = float('inf')
        
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)  # max heap using negative
            total_quality += q
            
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)  # subtract largest q
            
            if len(max_heap) == k:
                res = min(res, total_quality * ratio)
        
        return res