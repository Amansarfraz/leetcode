import bisect

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        products.sort()

        res = []
        prefix = ""

        for ch in searchWord:
            prefix += ch

            i = bisect.bisect_left(products, prefix)

            cur = []
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    cur.append(products[j])

            res.append(cur)

        return res