class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Square every number in the array
        squares = [x * x for x in nums]
        
        # Step 2: Sort the squares in ascending order
        squares.sort()
        
        # Step 3: Find the split point (the smallest n // 2 elements will be subtracted)
        m = len(squares) // 2
        
        ans = 0
        for i in range(len(squares)):
            if i < m:
                ans -= squares[i]  # Subtract smaller squares
            else:
                ans += squares[i]  # Add larger squares
                
        return ans
