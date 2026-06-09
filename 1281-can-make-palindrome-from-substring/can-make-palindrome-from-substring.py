class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prefix = [0]

        mask = 0
        for ch in s:
            mask ^= 1 << (ord(ch) - ord('a'))
            prefix.append(mask)

        ans = []

        for left, right, k in queries:
            mask = prefix[right + 1] ^ prefix[left]
            odd = bin(mask).count('1')
            ans.append(odd // 2 <= k)

        return ans