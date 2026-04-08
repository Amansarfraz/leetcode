import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # Pair capital with corresponding profits and sort by capital
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        
        max_heap = []
        i = 0
        n = len(profits)
        
        for _ in range(k):
            # Push all affordable projects into max heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # max heap via negative profit
                i += 1
            
            if not max_heap:
                break  # no projects can be done
            
            # Choose project with max profit
            w += -heapq.heappop(max_heap)
        
        return w