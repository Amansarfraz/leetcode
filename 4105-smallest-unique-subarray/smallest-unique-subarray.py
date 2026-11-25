class Solution(object):
    def smallestUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1

        # Coordinate compression (1 se m tak integers)
        uniq_vals = sorted(set(nums))
        rank_map = {v: i + 1 for i, v in enumerate(uniq_vals)}
        s = [rank_map[x] for x in nums]

        # Suffix Array via prefix doubling - O(n log n)
        sa = list(range(n))
        rk = s[:]
        tmp = [0] * n

        k = 1
        while k < n:
            sa.sort(key=lambda i: (rk[i], rk[i + k] if i + k < n else 0))
            tmp[sa[0]] = 1
            for i in range(1, n):
                prev_i, curr_i = sa[i - 1], sa[i]
                prev_key = (rk[prev_i], rk[prev_i + k] if prev_i + k < n else 0)
                curr_key = (rk[curr_i], rk[curr_i + k] if curr_i + k < n else 0)
                tmp[curr_i] = tmp[prev_i] + (1 if curr_key != prev_key else 0)
            rk = tmp[:]
            if rk[sa[n - 1]] == n:
                break
            k <<= 1

        # Rank array (pos[i] = sa mein index i ki position)
        pos = [0] * n
        for i, idx in enumerate(sa):
            pos[idx] = i

        # Kasai's LCP array - O(n)
        # lcp[i] = LCP between sa[i] and sa[i + 1]
        lcp = [0] * (n - 1)
        h = 0
        for i in range(n):
            if pos[i] == n - 1:
                h = 0
                continue
            j = sa[pos[i] + 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[pos[i]] = h
            if h > 0:
                h -= 1

        # Har suffix ke liye shortest unique prefix length nikalen
        ans = n
        for i in range(n):
            p = pos[i]
            max_lcp = 0
            if p > 0 and lcp[p - 1] > max_lcp:
                max_lcp = lcp[p - 1]
            if p < n - 1 and lcp[p] > max_lcp:
                max_lcp = lcp[p]

            needed = max_lcp + 1
            if needed <= n - i and needed < ans:
                ans = needed

        return ans