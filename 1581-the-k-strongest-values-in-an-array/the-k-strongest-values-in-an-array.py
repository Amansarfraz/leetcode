class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]

        left, right = 0, n - 1
        ans = []

        while len(ans) < k:
            left_strength = abs(arr[left] - median)
            right_strength = abs(arr[right] - median)

            if right_strength > left_strength:
                ans.append(arr[right])
                right -= 1
            elif right_strength < left_strength:
                ans.append(arr[left])
                left += 1
            else:
                if arr[right] > arr[left]:
                    ans.append(arr[right])
                    right -= 1
                else:
                    ans.append(arr[left])
                    left += 1

        return ans