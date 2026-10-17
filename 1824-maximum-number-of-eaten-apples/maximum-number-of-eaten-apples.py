import heapq

class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        min_heap = []  # Stores tuples of (rot_day, apple_count)
        eaten = 0
        i = 0
        n = len(apples)
        
        # Loop continues while we are still within the n days OR there are unrotten apples left in the heap
        while i < n or min_heap:
            # Step 1: Add today's newly grown apples to the heap (if within the first n days)
            if i < n and apples[i] > 0:
                # Rot day calculation: today's index (i) + its survival duration (days[i])
                rot_day = i + days[i]
                heapq.heappush(min_heap, (rot_day, apples[i]))
            
            # Step 2: Discard all apples that have already rotten by today
            while min_heap and min_heap[0][0] <= i:
                heapq.heappop(min_heap)
            
            # Step 3: Greedily eat the apple with the earliest expiration day
            if min_heap:
                rot_day, count = heapq.heappop(min_heap)
                eaten += 1
                count -= 1
                # If there are remaining apples left in this batch, push them back
                if count > 0:
                    heapq.heappush(min_heap, (rot_day, count))
            
            # Move to the next day
            i += 1
            
        return eaten
