class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        n = len(arr)

        # Right se pehla decreasing point find karo
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:

                # Right side me largest smaller element find karo
                j = n - 1

                while arr[j] >= arr[i] or (j > 0 and arr[j] == arr[j - 1]):
                    j -= 1

                # Swap
                arr[i], arr[j] = arr[j], arr[i]
                break

        return arr