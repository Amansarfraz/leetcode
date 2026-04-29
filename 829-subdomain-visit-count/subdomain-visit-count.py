class Solution(object):
    def subdomainVisits(self, cpdomains):
        count_map = {}
        
        for entry in cpdomains:
            count_str, domain = entry.split()
            count = int(count_str)
            
            parts = domain.split('.')
            
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                count_map[subdomain] = count_map.get(subdomain, 0) + count
        
        result = []
        for dom in count_map:
            result.append(str(count_map[dom]) + " " + dom)
        
        return result