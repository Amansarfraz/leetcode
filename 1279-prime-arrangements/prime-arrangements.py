class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        def count_primes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            
            return sum(is_prime)
        
        def factorial(x):
            res = 1
            for i in range(2, x + 1):
                res = (res * i) % MOD
            return res
        
        p = count_primes(n)
        
        return (factorial(p) * factorial(n - p)) % MOD