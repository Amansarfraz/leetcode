class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()

        for email in emails:
            local, domain = email.split('@')

            # remove everything after '+'
            if '+' in local:
                local = local[:local.index('+')]

            # remove dots
            local = local.replace('.', '')

            cleaned = local + '@' + domain
            seen.add(cleaned)

        return len(seen)