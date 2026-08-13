class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.s = list(s)
        # 4 * n is the standard size bounding for a segment tree array
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.size = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1)

    def push_up(self, node, left_child, right_child, l, r, mid):
        self.size[node] = self.size[left_child] + self.size[right_child]
        
        # Default assignment inheriting purely from separated sub-segments
        self.max_len[node] = max(self.max_len[left_child], self.max_len[right_child])
        self.pref_len[node] = self.pref_len[left_child]
        self.suff_len[node] = self.suff_len[right_child]
        
        # Check if the split boundary characters match across the division line
        if self.s[mid] == self.s[mid + 1]:
            combined = self.suff_len[left_child] + self.pref_len[right_child]
            self.max_len[node] = max(self.max_len[node], combined)
            
            # Extend prefix length if the left child is fully composed of identical characters
            if self.pref_len[left_child] == self.size[left_child]:
                self.pref_len[node] = self.size[left_child] + self.pref_len[right_child]
                
            # Extend suffix length if the right child is fully composed of identical characters
            if self.suff_len[right_child] == self.size[right_child]:
                self.suff_len[node] = self.size[right_child] + self.suff_len[left_child]

    def build(self, node, l, r):
        if l == r:
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.size[node] = 1
            return
        
        mid = (l + r) // 2
        self.build(2 * node, l, mid)
        self.build(2 * node + 1, mid + 1, r)
        self.push_up(node, 2 * node, 2 * node + 1, l, r, mid)

    def update(self, node, l, r, idx, ch):
        if l == r:
            self.s[idx] = ch
            return
        
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, ch)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, ch)
            
        self.push_up(node, 2 * node, 2 * node + 1, l, r, mid)


class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        tree = SegmentTree(s)
        ans = []
        
        for ch, idx in zip(queryCharacters, queryIndices):
            tree.update(1, 0, tree.n - 1, idx, ch)
            # The maximum length for the entire string is always stored at the root node (index 1)
            ans.append(tree.max_len[1])
            
        return ans
