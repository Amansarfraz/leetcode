class Solution(object):
    def findAnagrams(self, s, p):
        from collections import Counter

        ns, np = len(s), len(p)
        if ns < np:
            return []

        p_count = Counter(p)
        s_count = Counter(s[:np])
        result = []

        # check the first window
        if s_count == p_count:
            result.append(0)

        # slide the window
        for i in range(np, ns):
            start_char = s[i - np]
            end_char = s[i]

            # add new char
            s_count[end_char] = s_count.get(end_char, 0) + 1
            # remove old char
            s_count[start_char] -= 1
            if s_count[start_char] == 0:
                del s_count[start_char]

            if s_count == p_count:
                result.append(i - np + 1)

        return result