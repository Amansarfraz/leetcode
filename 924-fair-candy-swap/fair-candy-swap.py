class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        
        diff = (sumA - sumB) // 2
        
        setA = set(aliceSizes)
        
        for y in bobSizes:
            if y + diff in setA:
                return [y + diff, y]