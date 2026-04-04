class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(n, curr, next_curr):
            # Count how many numbers are between curr and next_curr within 1..n
            steps = 0
            while curr <= n:
                steps += min(n + 1, next_curr) - curr
                curr *= 10
                next_curr *= 10
            return steps

        curr = 1
        k -= 1  # because we start from 1
        while k > 0:
            steps = count_steps(n, curr, curr + 1)
            if steps <= k:
                # Move to next sibling
                curr += 1
                k -= steps
            else:
                # Move to first child
                curr *= 10
                k -= 1
        return curr