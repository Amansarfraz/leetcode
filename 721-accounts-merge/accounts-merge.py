class Solution(object):
    def accountsMerge(self, accounts):
        
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Step 1: initialize parent for every email
        for acc in accounts:
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
        
        # Step 2: union emails in same account
        for acc in accounts:
            first_email = acc[1]
            for email in acc[2:]:
                union(first_email, email)
        
        # Step 3: group emails by root parent
        groups = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                root = find(email)
                if root not in groups:
                    groups[root] = (name, set())
                groups[root][1].add(email)
        
        # Step 4: build result
        res = []
        for root in groups:
            name, emails = groups[root]
            res.append([name] + sorted(list(emails)))
        
        return res