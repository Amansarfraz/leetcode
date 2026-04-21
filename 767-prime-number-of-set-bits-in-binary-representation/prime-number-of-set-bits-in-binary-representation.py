class Solution(object):
    def countPrimeSetBits(self, left, right):
        
        # helper to check prime
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True
        
        res = 0
        
        for num in range(left, right + 1):
            bits = bin(num).count('1')
            if is_prime(bits):
                res += 1
        
        return res