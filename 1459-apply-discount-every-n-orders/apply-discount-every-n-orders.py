class Cashier(object):

    def __init__(self, n, discount, products, prices):
        """
        :type n: int
        :type discount: int
        :type products: List[int]
        :type prices: List[int]
        """
        self.n = n
        self.discount = discount
        self.count = 0
        self.price_map = {}

        for p, price in zip(products, prices):
            self.price_map[p] = price

    def getBill(self, product, amount):
        """
        :type product: List[int]
        :type amount: List[int]
        :rtype: float
        """
        self.count += 1

        total = 0.0
        for p, a in zip(product, amount):
            total += self.price_map[p] * a

        if self.count % self.n == 0:
            total *= (100 - self.discount) / 100.0

        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product, amount)