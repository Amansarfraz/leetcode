class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.sum_val = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def _push_down(self, node, start, end):
        if self.lazy[node] == 0:
            return
        
        lazy_val = self.lazy[node]
        mid = (start + end) // 2
        left_child = 2 * node
        right_child = 2 * node + 1

        # Update left child
        left_len = mid - start + 1
        self.sum_sq[left_child] = (self.sum_sq[left_child] + 2 * lazy_val * self.sum_val[left_child] + lazy_val * lazy_val * left_len) % 1000000007
        self.sum_val[left_child] = (self.sum_val[left_child] + lazy_val * left_len) % 1000000007
        self.lazy[left_child] += lazy_val

        # Update right child
        right_len = end - mid
        self.sum_sq[right_child] = (self.sum_sq[right_child] + 2 * lazy_val * self.sum_val[right_child] + lazy_val * lazy_val * right_len) % 1000000007
        self.sum_val[right_child] = (self.sum_val[right_child] + lazy_val * right_len) % 1000000007
        self.lazy[right_child] += lazy_val

        self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l <= start and end <= r:
            length = end - start + 1
            self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.sum_val[node] + val * val * length) % 1000000007
            self.sum_val[node] = (self.sum_val[node] + val * length) % 1000000007
            self.lazy[node] += val
            return

        self._push_down(node, start, end)
        mid = (start + end) // 2
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)
            
        self.sum_val[node] = (self.sum_val[2 * node] + self.sum_val[2 * node + 1]) % 1000000007
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % 1000000007


class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        st = SegmentTree(n)
        
        last_seen = {}
        total_ans = 0
        
        for i, num in enumerate(nums):
            # If the number was seen before, we only increment from the index after its last occurrence
            prev_idx = last_seen.get(num, -1)
            
            # Increment the distinct count by 1 for all valid subarrays ending at index i
            st.update(1, 0, n - 1, prev_idx + 1, i, 1)
            
            # Track the last seen index of the current number
            last_seen[num] = i
            
            # The root of the segment tree (node 1) now holds the sum of squares for all subarrays ending at `i`
            total_ans = (total_ans + st.sum_sq[1]) % MOD
            
        return total_ans
