class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        possible_dups = 0
        last = n - 1

        i = 0
        while i <= last - possible_dups:
            if arr[i] == 0:
                if i == last - possible_dups:
                    arr[last] = 0
                    last -= 1
                    break
                possible_dups += 1
            i += 1

        j = last - possible_dups

        for i in range(j, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]