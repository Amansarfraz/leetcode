class Solution(object):
    def validIPAddress(self, queryIP):
        
        # Check IPv4
        def isIPv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            
            for p in parts:
                if not p or (p[0] == '0' and len(p) > 1):
                    return False
                if not p.isdigit():
                    return False
                if not 0 <= int(p) <= 255:
                    return False
            return True
        
        # Check IPv6
        def isIPv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            
            hexdigits = "0123456789abcdefABCDEF"
            
            for p in parts:
                if not (1 <= len(p) <= 4):
                    return False
                for ch in p:
                    if ch not in hexdigits:
                        return False
            return True
        
        if isIPv4(queryIP):
            return "IPv4"
        elif isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"