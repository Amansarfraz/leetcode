class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        count = {}
        ans = 0
        
        for right in range(len(fruits)):
            fruit = fruits[right]
            count[fruit] = count.get(fruit, 0) + 1
            
            # More than 2 fruit types
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                
                if count[left_fruit] == 0:
                    del count[left_fruit]
                
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans