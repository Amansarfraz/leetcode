class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0
        
        def check(k):
            prev_max = float('-inf')
            
            # Process each block of size k
            for start in range(0, n, k):
                block = nums[start:start + k]
                
                # Condition 1: Check cyclic sortability
                # Count drops circularly within the block
                drops = 0
                for i in range(k):
                    if block[i] < block[i - 1]: # block[-1] correctly references the last element
                        drops += 1
                
                if drops > 1:
                    return False
                
                # Condition 2: Check global sorting between blocks
                current_min = min(block)
                current_max = max(block)
                
                if current_min < prev_max:
                    return False
                
                prev_max = current_max
                
            return True

        # Find all valid divisors k
        for k in range(1, n + 1):
            if n % k == 0:
                if check(k):
                    ans += k
                    
        return ans
