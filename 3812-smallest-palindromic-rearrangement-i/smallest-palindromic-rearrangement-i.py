class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        mid = n // 2
        
        # 1. Take the first half of the string and sort it alphabetically
        left_half = sorted(list(s[:mid]))
        
        # 2. Reconstruct the sorted left half as a string
        sorted_left = "".join(left_half)
        
        # 3. Handle the middle character if the string length is odd
        mid_char = s[mid] if n % 2 != 0 else ""
        
        # 4. Concatenate: sorted left + middle character + reversed sorted left
        return sorted_left + mid_char + sorted_left[::-1]
