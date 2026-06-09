class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        parsed = []
        
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city, i))
        
        invalid = set()
        
        for i in range(len(parsed)):
            name1, time1, amount1, city1, idx1 = parsed[i]
            
            if amount1 > 1000:
                invalid.add(idx1)
            
            for j in range(i + 1, len(parsed)):
                name2, time2, amount2, city2, idx2 = parsed[j]
                
                if name1 == name2 and city1 != city2 and abs(time1 - time2) <= 60:
                    invalid.add(idx1)
                    invalid.add(idx2)
        
        return [transactions[i] for i in invalid]