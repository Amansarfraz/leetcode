class Solution(object):
    def consecutiveNumbersSum(self, n):
        count = 0
        k = 1
        
        while k * (k - 1) // 2 < n:
            if (n - k * (k - 1) // 2) % k == 0:
                x = (n - k * (k - 1) // 2) // k
                if x > 0:
                    count += 1
            k += 1
        
        return count