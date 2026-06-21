class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        filtered = []

        for r in restaurants:
            rid, rating, vegan, price, dist = r

            if veganFriendly == 1 and vegan == 0:
                continue
            if price > maxPrice or dist > maxDistance:
                continue

            filtered.append(r)

        # sort by rating desc, then id desc
        filtered.sort(key=lambda x: (-x[1], -x[0]))

        return [r[0] for r in filtered]