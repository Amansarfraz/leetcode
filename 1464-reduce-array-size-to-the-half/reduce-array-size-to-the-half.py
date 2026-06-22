class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        counts = sorted(freq.values(), reverse=True)

        removed = 0
        ans = 0
        target = len(arr) // 2

        for count in counts:
            removed += count
            ans += 1

            if removed >= target:
                return ans