class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        items = sorted(zip(values, labels), reverse=True)

        used = {}
        ans = 0
        taken = 0

        for value, label in items:
            if used.get(label, 0) < useLimit:
                ans += value
                used[label] = used.get(label, 0) + 1
                taken += 1

                if taken == numWanted:
                    break

        return ans