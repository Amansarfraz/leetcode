class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # position to write compressed character
        read = 0   # position to read characters
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            # Count consecutive characters
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if > 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write