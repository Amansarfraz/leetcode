class Solution(object):
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        # if left goes out of bounds, wrap around
        return letters[left % len(letters)]