class Solution(object):
    def validSequence(self, word1, word2):
        n1, n2 = len(word1), len(word2)
        
        # last[j] stores the maximum index in word1 that can match word2[j:]
        last = [-1] * n2
        i = n1 - 1
        j = n2 - 1
        
        # Step 1: Precompute the right-to-left matching positions
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1
            
        ans = []
        j = 0
        changed = False
        
        # Step 2: Greedily build the lexicographically smallest sequence
        for i in range(n1):
            if j == n2:
                break
                
            # Case 1: The characters match perfectly
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Case 2: Mismatch, try using the single allowed modification
            elif not changed:
                # Check if the rest of word2 can be successfully matched
                if j + 1 == n2 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    changed = True
                    
        return ans if len(ans) == n2 else []
