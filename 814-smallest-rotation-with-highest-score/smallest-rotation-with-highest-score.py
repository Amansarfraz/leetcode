class Solution(object):
    def bestRotation(self, nums):
        n = len(nums)
        change = [0] * (n + 1)
        
        for i, num in enumerate(nums):
            # start and end of valid k range
            start = (i + 1) % n
            end = (i - num + n + 1) % n
            
            change[start] += 1
            change[end] -= 1
            
            if start > end:
                change[0] += 1
        
        max_score = -1
        score = 0
        best_k = 0
        
        for k in range(n):
            score += change[k]
            if score > max_score:
                max_score = score
                best_k = k
        
        return best_k