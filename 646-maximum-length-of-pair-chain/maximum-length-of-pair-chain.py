class Solution(object):
    def findLongestChain(self, pairs):
        # sort by ending value
        pairs.sort(key=lambda x: x[1])

        count = 0
        last_end = float('-inf')

        for start, end in pairs:
            if start > last_end:
                count += 1
                last_end = end

        return count