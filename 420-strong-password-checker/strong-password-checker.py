class Solution(object):
    def strongPasswordChecker(self, s):
        n = len(s)
        
        # Check missing types
        missing_lower = missing_upper = missing_digit = 1
        for c in s:
            if c.islower(): missing_lower = 0
            elif c.isupper(): missing_upper = 0
            elif c.isdigit(): missing_digit = 0
        missing_types = missing_lower + missing_upper + missing_digit

        # Count repeating sequences
        repeats = []
        i = 0
        while i < n:
            j = i
            while i < n and s[i] == s[j]:
                i += 1
            repeats.append(i - j)

        # Short case
        if n < 6:
            return max(6 - n, missing_types)

        # Count replacements
        replace = 0
        one = two = 0

        for r in repeats:
            if r >= 3:
                replace += r // 3
                if r % 3 == 0:
                    one += 1
                elif r % 3 == 1:
                    two += 1

        # Medium case
        if n <= 20:
            return max(replace, missing_types)

        # Long case
        delete = n - 20

        # Step 1: remove from mod 0 groups
        use = min(delete, one)
        replace -= use
        delete -= use

        # Step 2: remove from mod 1 groups
        use = min(delete // 2, two)
        replace -= use
        delete -= use * 2

        # Step 3: remove from remaining groups
        use = delete // 3
        replace -= use

        return (n - 20) + max(replace, missing_types)