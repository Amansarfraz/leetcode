class Solution(object):
    def shoppingOffers(self, price, special, needs):
        memo = {}

        def dfs(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]

            # 🔹 Cost without any offer
            cost = sum(needs[i] * price[i] for i in range(len(needs)))

            # 🔹 Try each special offer
            for offer in special:
                new_needs = []
                for i in range(len(needs)):
                    if offer[i] > needs[i]:
                        break
                    new_needs.append(needs[i] - offer[i])
                else:
                    cost = min(cost, offer[-1] + dfs(new_needs))

            memo[tuple(needs)] = cost
            return cost

        return dfs(needs)