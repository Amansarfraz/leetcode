class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()

        min_diff = float('inf')
        ans = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff < min_diff:
                min_diff = diff
                ans = [[arr[i - 1], arr[i]]]
            elif diff == min_diff:
                ans.append([arr[i - 1], arr[i]])

        return ans