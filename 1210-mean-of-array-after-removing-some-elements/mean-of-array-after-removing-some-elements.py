class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """

        arr.sort()

        n = len(arr)

        remove = n // 20

        trimmed = arr[remove:n - remove]

        return sum(trimmed) / float(len(trimmed))

