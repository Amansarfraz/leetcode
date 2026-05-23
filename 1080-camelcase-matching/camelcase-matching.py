class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        
        # Function to check one query
        def match(query, pattern):
            
            i = 0
            
            for ch in query:
                
                # Character matches pattern
                if i < len(pattern) and ch == pattern[i]:
                    i += 1
                
                # Extra uppercase character not allowed
                elif ch.isupper():
                    return False
            
            # Entire pattern must be matched
            return i == len(pattern)
        
        
        result = []
        
        for query in queries:
            result.append(match(query, pattern))
        
        return result