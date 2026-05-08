class Solution(object):
    def superpalindromesInRange(self, left, right):
        L = int(left)
        R = int(right)

        def is_palindrome(x):
            s = str(x)
            return s == s[::-1]

        ans = 0

        # Generate palindromic roots
        for k in range(1, 100000):

            s = str(k)

            # Odd length palindrome
            odd = int(s + s[-2::-1])
            sq = odd * odd

            if L <= sq <= R and is_palindrome(sq):
                ans += 1

            # Even length palindrome
            even = int(s + s[::-1])
            sq = even * even

            if L <= sq <= R and is_palindrome(sq):
                ans += 1

        return ans