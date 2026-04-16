class Solution(object):
    def isPossible(self, nums):
        from collections import Counter, defaultdict
        
        count = Counter(nums)
        end = defaultdict(int)
        
        for num in nums:
            if count[num] == 0:
                continue
            
            count[num] -= 1
            
            # Case 1: extend existing subsequence
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            
            # Case 2: create new subsequence of length 3
            elif count[num + 1] > 0 and count[num + 2] > 0:
                count[num + 1] -= 1
                count[num + 2] -= 1
                end[num + 2] += 1
            
            # Case 3: not possible
            else:
                return False
        
        return True