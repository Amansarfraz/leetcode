class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        cnt = {'c': 0, 'r': 0, 'o': 0, 'a': 0}
        frogs = 0
        ans = 0

        for ch in croakOfFrogs:
            if ch == 'c':
                cnt['c'] += 1
                frogs += 1
                ans = max(ans, frogs)

            elif ch == 'r':
                if cnt['c'] == 0:
                    return -1
                cnt['c'] -= 1
                cnt['r'] += 1

            elif ch == 'o':
                if cnt['r'] == 0:
                    return -1
                cnt['r'] -= 1
                cnt['o'] += 1

            elif ch == 'a':
                if cnt['o'] == 0:
                    return -1
                cnt['o'] -= 1
                cnt['a'] += 1

            else:  # 'k'
                if cnt['a'] == 0:
                    return -1
                cnt['a'] -= 1
                frogs -= 1

        if frogs != 0:
            return -1

        return ans