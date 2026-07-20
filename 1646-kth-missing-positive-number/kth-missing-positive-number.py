class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        current = 1
        i = 0

        while k > 0:
            if i < len(arr) and arr[i] == current:
                i += 1
            else:
                k -= 1
                if k == 0:
                    return current
            current += 1