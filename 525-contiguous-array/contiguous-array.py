class Solution(object):
    def findMaxLength(self, nums):
        sum_to_index = {0: -1}  # prefix_sum -> first index
        max_len = 0
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            if prefix_sum in sum_to_index:
                max_len = max(max_len, i - sum_to_index[prefix_sum])
            else:
                sum_to_index[prefix_sum] = i
        
        return max_len