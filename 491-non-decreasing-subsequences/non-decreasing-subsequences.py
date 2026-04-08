class Solution(object):
    def findSubsequences(self, nums):
        res = []
        
        def dfs(start, path):
            if len(path) >= 2:
                res.append(path[:])
            
            used = set()  # 🔥 avoid duplicates at same level
            
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                
                # ensure non-decreasing
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    
                    dfs(i + 1, path)
                    
                    path.pop()
        
        dfs(0, [])
        return res