class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        changes = [0] * 1001  # locations are in range [0, 1000]

        for passengers, start, end in trips:
            changes[start] += passengers
            changes[end] -= passengers

        current_passengers = 0

        for change in changes:
            current_passengers += change
            if current_passengers > capacity:
                return False

        return True