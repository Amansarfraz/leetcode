class Solution(object):
    def makeArrayIncreasing(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        from bisect import bisect_right

        arr2 = sorted(set(arr2))
        dp = {-float('inf'): 0}

        for x in arr1:
            ndp = {}

            for prev, ops in dp.items():
                if x > prev:
                    if x not in ndp or ndp[x] > ops:
                        ndp[x] = ops

                idx = bisect_right(arr2, prev)
                if idx < len(arr2):
                    y = arr2[idx]
                    if y not in ndp or ndp[y] > ops + 1:
                        ndp[y] = ops + 1

            dp = ndp
            if not dp:
                return -1

        return min(dp.values())