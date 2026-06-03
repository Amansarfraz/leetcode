class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        freq = {}

        for num in arr1:
            freq[num] = freq.get(num, 0) + 1

        ans = []

        for num in arr2:
            ans.extend([num] * freq.pop(num))

        for num in sorted(freq):
            ans.extend([num] * freq[num])

        return ans