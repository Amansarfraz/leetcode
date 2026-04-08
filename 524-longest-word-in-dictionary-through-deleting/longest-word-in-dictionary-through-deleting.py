class Solution(object):
    def findLongestWord(self, s, dictionary):
        def isSubsequence(word):
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            return i == len(word)
        
        # Sort dictionary by length descending, then lex
        dictionary.sort(key=lambda x: (-len(x), x))
        
        for word in dictionary:
            if isSubsequence(word):
                return word
        return ""