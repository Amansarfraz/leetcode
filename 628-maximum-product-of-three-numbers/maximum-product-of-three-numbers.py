class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        
        # Case 1: 3 largest numbers
        case1 = nums[-1] * nums[-2] * nums[-3]
        
        # Case 2: 2 smallest + largest
        case2 = nums[0] * nums[1] * nums[-1]
        
        return max(case1, case2)