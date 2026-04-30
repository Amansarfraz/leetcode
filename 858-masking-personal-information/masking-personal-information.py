class Solution(object):
    def maskPII(self, s):
        s = s.lower()
        
        # EMAIL CASE
        if '@' in s:
            name, domain = s.split('@')
            return name[0] + "*****" + name[-1] + "@" + domain
        
        # PHONE CASE
        digits = []
        for ch in s:
            if ch.isdigit():
                digits.append(ch)
        
        local = "***-***-" + "".join(digits[-4:])
        
        if len(digits) == 10:
            return local
        
        country = "+" + "*" * (len(digits) - 10)
        return country + "-" + local