class Solution(object):
    def maximumSwap(self, num):
        digits = list(str(num))
        
        # store last position of each digit
        last = {int(d): i for i, d in enumerate(digits)}
        
        for i in range(len(digits)):
            curr = int(digits[i])
            
            # try bigger digits from 9 → curr+1
            for d in range(9, curr, -1):
                if d in last and last[d] > i:
                    # swap
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        
        return num