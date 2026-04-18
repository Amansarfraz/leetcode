class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums:
            return 0

        from collections import Counter

        count = Counter(nums)
        values = sorted(count.keys())

        prev = None
        take = 0
        skip = 0

        for v in values:
            curr_points = v * count[v]

            if prev == v - 1:
                # adjacent → can't take both
                take_new = skip + curr_points
                skip_new = max(skip, take)
            else:
                # not adjacent → free to take
                take_new = max(skip, take) + curr_points
                skip_new = max(skip, take)

            take, skip = take_new, skip_new
            prev = v

        return max(take, skip)