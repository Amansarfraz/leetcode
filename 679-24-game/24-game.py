class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    next_nums = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    a, b = nums[i], nums[j]

                    candidates = [a + b, a - b, b - a, a * b]

                    if abs(b) > 1e-6:
                        candidates.append(a / b)
                    if abs(a) > 1e-6:
                        candidates.append(b / a)

                    for val in candidates:
                        next_nums.append(val)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()

            return False

        return dfs([float(x) for x in cards])