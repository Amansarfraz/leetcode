class Solution(object):
    def findKthNumber(self, m, n, k):
        def countLessEqual(x):
            count = 0
            for i in range(1, m + 1):
                count += min(n, x // i)
            return count
        
        left, right = 1, m * n
        
        while left < right:
            mid = (left + right) // 2
            
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        return left