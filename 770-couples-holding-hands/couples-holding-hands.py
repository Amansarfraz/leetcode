class Solution(object):
    def minSwapsCouples(self, row):
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        
        for i in range(0, len(row), 2):
            first = row[i]
            partner = first ^ 1   # partner of x is x ^ 1
            
            if row[i + 1] != partner:
                swaps += 1
                
                # index where partner is sitting
                partner_index = pos[partner]
                
                # swap
                row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
                
                # update positions
                pos[row[partner_index]] = partner_index
                pos[row[i + 1]] = i + 1
        
        return swaps