class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        # Pair each stone's total value weight along with individual values
        # Each element will be: (aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i])
        stones = []
        for a, b in zip(aliceValues, bobValues):
            stones.append((a + b, a, b))
            
        # Sort stones by combined value in descending order
        stones.sort(key=lambda x: x[0], reverse=True)
        
        alice_score = 0
        bob_score = 0
        
        # Turn-based allocation
        for i, (total, a, b) in enumerate(stones):
            if i % 2 == 0:
                alice_score += a  # Alice's turn
            else:
                bob_score += b    # Bob's turn
                
        # Determine the winner
        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1
        else:
            return 0
