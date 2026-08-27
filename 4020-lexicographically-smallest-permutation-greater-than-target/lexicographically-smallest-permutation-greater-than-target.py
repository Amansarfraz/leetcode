class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        if len(s) != len(target):
            return ""
            
        # Count the frequency of each character in s
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1
            
        n = len(s)
        ans = []
        
        def backtrack(idx, is_greater):
            # Base case: We reached the end. 
            # It is only a valid answer if we are strictly greater than target.
            if idx == n:
                return is_greater
                
            # If we are already strictly greater, pick the smallest available character greedily
            if is_greater:
                for i in range(26):
                    if counts[i] > 0:
                        counts[i] -= 1
                        ans.append(chr(ord('a') + i))
                        if backtrack(idx + 1, True):
                            return True
                        ans.pop()
                        counts[i] += 1
                return False
            
            # If we are still matching target's prefix
            target_idx = ord(target[idx]) - ord('a')
            
            # 1. Try matching the exact character at target[idx] to stay equal for now
            if counts[target_idx] > 0:
                counts[target_idx] -= 1
                ans.append(target[idx])
                if backtrack(idx + 1, False):
                    return True
                ans.pop()
                counts[target_idx] += 1
                
            # 2. Try choosing a character strictly greater than target[idx] to break the tie
            for i in range(target_idx + 1, 26):
                if counts[i] > 0:
                    counts[i] -= 1
                    ans.append(chr(ord('a') + i))
                    if backtrack(idx + 1, True):
                        return True
                    ans.pop()
                    counts[i] += 1
                    
            return False

        if backtrack(0, False):
            return "".join(ans)
        return ""
