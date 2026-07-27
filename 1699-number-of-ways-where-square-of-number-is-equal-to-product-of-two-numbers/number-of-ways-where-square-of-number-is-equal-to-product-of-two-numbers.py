class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        from collections import Counter

        def count(a, b):
            freq = Counter(b)
            ans = 0

            for x in a:
                target = x * x
                for y in freq:
                    if target % y != 0:
                        continue
                    z = target // y
                    if z not in freq:
                        continue
                    if y == z:
                        ans += freq[y] * (freq[y] - 1) // 2
                    elif y < z:
                        ans += freq[y] * freq[z]
            return ans

        return count(nums1, nums2) + count(nums2, nums1)