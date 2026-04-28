class Solution(object):
    def preimageSizeFZF(self, k):
        
        def countZeros(x):
            res = 0
            while x > 0:
                x //= 5
                res += x
            return res
        
        # Binary search: first x such that f(x) >= k
        def find(k):
            left, right = 0, 5 * (k + 1)
            
            while left < right:
                mid = (left + right) // 2
                if countZeros(mid) < k:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        return find(k + 1) - find(k)