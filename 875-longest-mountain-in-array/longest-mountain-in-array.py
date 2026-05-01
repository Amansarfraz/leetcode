class Solution(object):
    def longestMountain(self, arr):

        n = len(arr)
        longest = 0
        i = 1

        while i < n - 1:

            # check if arr[i] is peak
            if arr[i-1] < arr[i] > arr[i+1]:

                left = i - 1
                right = i + 1

                # go left (increasing)
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1

                # go right (decreasing)
                while right < n - 1 and arr[right] > arr[right+1]:
                    right += 1

                longest = max(longest, right - left + 1)

                i = right   # skip processed part

            else:
                i += 1

        return longest