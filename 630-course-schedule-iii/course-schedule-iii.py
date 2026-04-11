import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        # Sort by last day
        courses.sort(key=lambda x: x[1])
        
        max_heap = []
        total_time = 0
        
        for duration, lastDay in courses:
            total_time += duration
            heapq.heappush(max_heap, -duration)  # max heap
            
            # If we exceed deadline, remove longest course
            if total_time > lastDay:
                longest = -heapq.heappop(max_heap)
                total_time -= longest
        
        return len(max_heap)