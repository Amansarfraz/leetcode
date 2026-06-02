class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        path = []

        while label >= 1:
            path.append(label)

            level = label.bit_length() - 1
            start = 1 << level
            end = (1 << (level + 1)) - 1

            label = (start + end - label) // 2

        return path[::-1]
        