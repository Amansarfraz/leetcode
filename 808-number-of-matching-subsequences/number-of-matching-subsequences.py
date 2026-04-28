class Solution(object):
    def numMatchingSubseq(self, s, words):
        from collections import defaultdict, deque
        
        waiting = defaultdict(deque)
        
        # Initialize: put each word in bucket of its first char
        for word in words:
            waiting[word[0]].append(word)
        
        count = 0
        
        for ch in s:
            old_bucket = waiting[ch]
            waiting[ch] = deque()
            
            while old_bucket:
                word = old_bucket.popleft()
                
                if len(word) == 1:
                    count += 1
                else:
                    # Move remaining substring to next required char
                    waiting[word[1]].append(word[1:])
        
        return count