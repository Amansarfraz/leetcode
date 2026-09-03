class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the first occurrence index of each character
        first_seen = {}
        max_len = -1
        
        for index, char in enumerate(s):
            if char in first_seen:
                # If we've seen it before, calculate the distance between current index and the first index
                current_len = index - first_seen[char] - 1
                max_len = max(max_len, current_len)
            else:
                # Store the index of the first time we see this character
                first_seen[char] = index
                
        return max_len
