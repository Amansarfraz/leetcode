class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        ans = 0

        for x in arr1:
            valid = True
            for y in arr2:
                if abs(x - y) <= d:
                    valid = False
                    break
            if valid:
                ans += 1

        return ans