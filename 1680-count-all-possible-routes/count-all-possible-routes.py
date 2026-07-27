class Solution(object):
    def countRoutes(self, locations, start, finish, fuel):
        """
        :type locations: List[int]
        :type start: int
        :type finish: int
        :type fuel: int
        :rtype: int
        """
        MOD = 10**9 + 7
        memo = {}

        def dfs(city, fuel_left):
            if (city, fuel_left) in memo:
                return memo[(city, fuel_left)]

            ans = 1 if city == finish else 0

            for nxt in range(len(locations)):
                if nxt != city:
                    cost = abs(locations[city] - locations[nxt])
                    if cost <= fuel_left:
                        ans = (ans + dfs(nxt, fuel_left - cost)) % MOD

            memo[(city, fuel_left)] = ans
            return ans

        return dfs(start, fuel)