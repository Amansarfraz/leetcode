import math

class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Validate that t only contains prime factors 2, 3, 5, 7
        temp_t = t
        for d in (2, 3, 5, 7):
            while temp_t % d == 0:
                temp_t //= d
        if temp_t > 1:
            return "-1"
            
        n = len(num)
        
        # Helper to find the minimal suffix required to satisfy a target value `rem` 
        def get_min_suffix(rem, free_slots):
            factors = []
            for d in (9, 8, 7, 6, 5, 4, 3, 2):
                while rem % d == 0:
                    factors.append(str(d))
                    rem //= d
            if rem > 1:
                return None
            if len(factors) > free_slots:
                return None
            # Fill remaining spots with '1's and sort digits ascendingly
            factors.extend(['1'] * (free_slots - len(factors)))
            factors.sort()
            return "".join(factors)

        # 1. Check if the original number itself is valid
        if '0' not in num:
            prod = 1
            for char in num:
                prod = (prod * int(char))
            if prod % t == 0:
                return num

        # Precompute the prefix remaining target values for t
        rem_t = [t] * (n + 1)
        first_zero = n
        for i in range(n):
            digit = int(num[i])
            if digit == 0:
                first_zero = i
                break
            rem_t[i + 1] = rem_t[i] // gcd(rem_t[i], digit)

        # 2. Try to change a digit from right to left to make it larger
        # We start searching from the position of the first zero (or n-1 if no zero)
        start_idx = min(n - 1, first_zero)
        for i in range(start_idx, -1, -1):
            start_digit = int(num[i]) + 1
            for d in range(start_digit, 10):
                next_rem = rem_t[i] // gcd(rem_t[i], d)
                suffix = get_min_suffix(next_rem, n - 1 - i)
                if suffix is not None:
                    return num[:i] + str(d) + suffix

        # 3. If no same-length solution works, find the absolute minimum length needed for t
        factors = []
        temp = t
        for d in (9, 8, 7, 6, 5, 4, 3, 2):
            while temp % d == 0:
                factors.append(str(d))
                temp //= d
                
        req_len = max(n + 1, len(factors))
        return get_min_suffix(t, req_len)
