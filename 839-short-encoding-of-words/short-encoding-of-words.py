class Solution(object):
    def minimumLengthEncoding(self, words):
        words = set(words)
        
        for word in list(words):
            # remove all suffixes
            for i in range(1, len(word)):
                words.discard(word[i:])
        
        # each word contributes len + 1 (#)
        return sum(len(word) + 1 for word in words)