class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """

        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [float('inf')] * n

        left = 0
        current_sum = 0
        ans = float('inf')
        min_length = float('inf')

        for right in range(n):
            current_sum += arr[right]

            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            if current_sum == target:
                length = right - left + 1

                # Check if there is a previous non-overlapping subarray
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])

                min_length = min(min_length, length)

            best[right] = min_length

        return -1 if ans == float('inf') else ans