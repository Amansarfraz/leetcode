class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        keep = arr[0]
        delete = float('-inf')
        ans = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]
            prev_keep = keep

            keep = max(keep + x, x)
            delete = max(delete + x, prev_keep)

            ans = max(ans, keep, delete)

        return ans