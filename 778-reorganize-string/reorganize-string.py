class Solution(object):
    def reorganizeString(self, s):
        from collections import Counter
        import heapq
        
        count = Counter(s)
        
        # max heap (use negative counts)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        
        prev = (0, '')  # (count, char)
        result = []
        
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char)
            
            # push previous back if still remaining
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            
            # decrease current freq
            freq += 1
            prev = (freq, char)
        
        result_str = "".join(result)
        
        # check valid
        if len(result_str) != len(s):
            return ""
        
        return result_str