class Solution(object):
    def primePalindrome(self, n):
        
        # Check prime
        def isPrime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            i = 3
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 2
            return True
        
        # Special case
        if 8 <= n <= 11:
            return 11
        
        # Generate odd-length palindromes
        length = 1
        while True:
            for root in range(10**(length - 1), 10**length):
                s = str(root)
                # Create palindrome (odd length)
                pal = int(s + s[-2::-1])
                
                if pal >= n and isPrime(pal):
                    return pal
            
            length += 1