class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        n = len(arr)

        if m == n:
            return n

        length = [0] * (n + 2)
        count = [0] * (n + 1)

        ans = -1

        for step, pos in enumerate(arr, 1):
            left = length[pos - 1]
            right = length[pos + 1]

            new_len = left + right + 1

            if left:
                count[left] -= 1
            if right:
                count[right] -= 1

            count[new_len] += 1

            length[pos - left] = new_len
            length[pos + right] = new_len

            if count[m] > 0:
                ans = step

        return ans