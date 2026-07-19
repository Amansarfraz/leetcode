class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        winner = arr[0]
        streak = 0
        maximum = max(arr)

        if k >= len(arr):
            return maximum

        for i in range(1, len(arr)):
            if winner > arr[i]:
                streak += 1
            else:
                winner = arr[i]
                streak = 1

            if streak == k:
                return winner

        return winner