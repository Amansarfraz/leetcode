class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ones = sum(arr)

        if ones == 0:
            return [0, 2]

        if ones % 3 != 0:
            return [-1, -1]

        k = ones // 3
        first = second = third = -1
        count = 0

        for i, bit in enumerate(arr):
            if bit == 1:
                count += 1

                if count == 1:
                    first = i
                elif count == k + 1:
                    second = i
                elif count == 2 * k + 1:
                    third = i

        length = len(arr) - third

        if (first + length <= second and
            second + length <= third):

            if (arr[first:first + length] ==
                arr[second:second + length] ==
                arr[third:third + length]):

                return [first + length - 1,
                        second + length]

        return [-1, -1]