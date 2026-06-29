from collections import defaultdict

class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        diagonals = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])

        ans = []

        for d in sorted(diagonals.keys()):
            ans.extend(reversed(diagonals[d]))

        return ans