class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Define the set of all vowels (both lowercase and uppercase)
        vowels = set("aeiouAEIOU")
        
        # Find the midpoint of the string
        mid = len(s) // 2
        
        # Split the string into two halves
        left_half = s[:mid]
        right_half = s[mid:]
        
        # Count vowels in both halves
        left_vowel_count = sum(1 for char in left_half if char in vowels)
        right_vowel_count = sum(1 for char in right_half if char in vowels)
        
        # Return True if counts are alike, False otherwise
        return left_vowel_count == right_vowel_count
