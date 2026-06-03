class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff = [0] * (n + 1)

        for first, last, seats in bookings:
            diff[first - 1] += seats
            if last < n:
                diff[last] -= seats

        ans = [0] * n
        ans[0] = diff[0]

        for i in range(1, n):
            ans[i] = ans[i - 1] + diff[i]

        return ans