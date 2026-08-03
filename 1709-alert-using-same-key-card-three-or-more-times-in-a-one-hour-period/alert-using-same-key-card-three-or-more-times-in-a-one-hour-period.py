from collections import defaultdict

class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        mp = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            h, m = map(int, time.split(":"))
            mp[name].append(h * 60 + m)

        ans = []

        for name in mp:
            times = sorted(mp[name])

            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    ans.append(name)
                    break

        return sorted(ans)