class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if not set(s2).issubset(set(s1)):
            return 0
        
        index2 = 0
        count1 = 0
        count2 = 0
        
        recall = {}
        
        while count1 < n1:
            count1 += 1
            
            for ch in s1:
                if ch == s2[index2]:
                    index2 += 1
                    if index2 == len(s2):
                        index2 = 0
                        count2 += 1
            
            # cycle detection
            if index2 in recall:
                prev_count1, prev_count2 = recall[index2]
                
                cycle_s1 = count1 - prev_count1
                cycle_s2 = count2 - prev_count2
                
                remaining = n1 - count1
                times = remaining // cycle_s1
                
                count1 += times * cycle_s1
                count2 += times * cycle_s2
            else:
                recall[index2] = (count1, count2)
        
        return count2 // n2