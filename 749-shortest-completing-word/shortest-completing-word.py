class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        from collections import Counter
        
        # Step 1: count letters in licensePlate
        need = Counter(c.lower() for c in licensePlate if c.isalpha())
        
        result = None
        
        # Step 2: check each word
        for word in words:
            count = Counter(word.lower())
            
            # check if word satisfies all requirements
            if all(count[c] >= need[c] for c in need):
                if result is None or len(word) < len(result):
                    result = word
        
        return result