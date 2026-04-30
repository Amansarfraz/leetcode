class Solution(object):
    def numFriendRequests(self, ages):
        ages.sort()
        n = len(ages)
        
        res = 0
        left = 0
        right = 0
        
        for i in range(n):
            ageA = ages[i]
            
            if ageA < 15:
                continue
            
            # Move left pointer
            while ages[left] <= 0.5 * ageA + 7:
                left += 1
            
            # Move right pointer
            while right < n and ages[right] <= ageA:
                right += 1
            
            res += right - left - 1
        
        return res