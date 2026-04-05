class Solution(object):
    def find132pattern(self, nums):
        stack = []
        third = float('-inf')  # nums[k] in 132 pattern
        
        # Traverse from right to left
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        
        return False