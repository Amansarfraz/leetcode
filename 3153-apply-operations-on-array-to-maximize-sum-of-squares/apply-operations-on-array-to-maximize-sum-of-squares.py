class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Determine the max bit length needed (up to 30 bits for 10^9 constraints)
        max_num = max(nums)
        max_bit_len = max_num.bit_length()
        
        # Step 1: Count how many numbers have a 1 at each bit position
        bit_counts = [0] * max_bit_len
        for num in nums:
            for i in range(max_bit_len):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        # Step 2: Greedily build the k largest possible numbers
        total_sum_of_squares = 0
        for _ in range(k):
            current_num = 0
            for i in range(max_bit_len):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1  # Use up one '1' bit
            
            # Add the square of this reconstructed number to our total
            total_sum_of_squares = (total_sum_of_squares + current_num * current_num) % MOD
            
        return total_sum_of_squares
