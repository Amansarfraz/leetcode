class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        
        ans = []
        prefix = ""
        
        for ch in searchWord:
            prefix += ch
            cur = []
            
            for product in products:
                if product.startswith(prefix):
                    cur.append(product)
                    if len(cur) == 3:
                        break
            
            ans.append(cur)
        
        return ans