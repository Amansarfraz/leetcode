class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        
        def devowel(word):
            vowels = "aeiou"
            return ''.join('*' if ch in vowels else ch for ch in word.lower())
        
        exact = set(wordlist)
        case_map = {}
        vowel_map = {}
        
        for word in wordlist:
            low = word.lower()
            
            if low not in case_map:
                case_map[low] = word
            
            dv = devowel(word)
            if dv not in vowel_map:
                vowel_map[dv] = word
        
        ans = []
        
        for q in queries:
            if q in exact:
                ans.append(q)
            else:
                low = q.lower()
                
                if low in case_map:
                    ans.append(case_map[low])
                else:
                    dv = devowel(q)
                    
                    if dv in vowel_map:
                        ans.append(vowel_map[dv])
                    else:
                        ans.append("")
        
        return ans