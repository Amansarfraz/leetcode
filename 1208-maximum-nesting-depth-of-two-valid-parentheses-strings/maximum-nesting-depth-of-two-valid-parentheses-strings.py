class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        answer = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Increment depth for an opening parenthesis
                answer.append(depth % 2)
                depth += 1
            else:
                # Decrement depth for a closing parenthesis
                depth -= 1
                answer.append(depth % 2)
                
        return answer
