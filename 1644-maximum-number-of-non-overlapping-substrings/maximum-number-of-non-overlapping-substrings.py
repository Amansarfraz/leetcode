class Solution(object):
    def maxNumOfSubstrings(self, s):
        """:type s: str :rtype: List[str]"""
        first = {c: s.find(c) for c in set(s)}
        last = {c: s.rfind(c) for c in set(s)}
        
        def get_valid_substring(i):
            right = last[s[i]]
            j = i
            while j <= right:
                c = s[j]
                if first[c] < i:
                    return -1
                right = max(right, last[c])
                j += 1
            return right

        intervals = []
        for i in range(len(s)):
            if i == first[s[i]]:
                r = get_valid_substring(i)
                if r != -1:
                    intervals.append([i, r])

        intervals.sort(key=lambda x: x[1])
        res = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                res.append(s[start:end + 1])
                prev_end = end
        return res
