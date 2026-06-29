from collections import defaultdict

class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        foods = set()
        tables = defaultdict(lambda: defaultdict(int))

        for _, table, food in orders:
            foods.add(food)
            tables[table][food] += 1

        foods = sorted(foods)

        ans = [["Table"] + foods]

        for table in sorted(tables, key=int):
            row = [table]
            for food in foods:
                row.append(str(tables[table][food]))
            ans.append(row)

        return ans