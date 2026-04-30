import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        
        # Extract words only (ignore punctuation)
        words = re.findall(r"[a-zA-Z]+", paragraph.lower())
        
        count = Counter()
        
        for word in words:
            if word not in banned_set:
                count[word] += 1
        
        return count.most_common(1)[0][0]