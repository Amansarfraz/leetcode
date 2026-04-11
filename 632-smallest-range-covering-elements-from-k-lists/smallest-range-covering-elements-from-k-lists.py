import heapq

class Solution(object):
    def smallestRange(self, nums):
        k = len(nums)
        heap = []
        current_max = float('-inf')
        
        # Step 1: initialize heap
        for i in range(k):
            val = nums[i][0]
            heap.append((val, i, 0))  # (value, list_index, element_index)
            current_max = max(current_max, val)
        
        heapq.heapify(heap)
        
        range_start, range_end = -10**9, 10**9
        
        while True:
            min_val, list_idx, elem_idx = heapq.heappop(heap)
            
            # Update smallest range
            if current_max - min_val < range_end - range_start:
                range_start, range_end = min_val, current_max
            
            # Move to next element in same list
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            next_val = nums[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
            
            current_max = max(current_max, next_val)
        
        return [range_start, range_end]